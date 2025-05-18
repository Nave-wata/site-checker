#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Entry point for running the scraper.
This script can be executed directly to run the scraping process.
"""

import argparse
import sys

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.example_spider import ExampleSpider
from scraper.spiders.link_follower_spider import LinkFollowerSpider


def parse_args():
    """
    Parse command line arguments.

    Returns:
        Namespace: The parsed arguments
    """
    parser = argparse.ArgumentParser(description='Run a Scrapy spider')

    # Spider selection
    parser.add_argument('--spider', type=str, default='link_follower',
                        help='Spider to run (default: link_follower)')

    # Spider parameters
    parser.add_argument('--start-urls', type=str,
                        help='Comma-separated list of start URLs')
    parser.add_argument('--allowed-domains', type=str,
                        help='Comma-separated list of allowed domains')

    # Scrapy settings
    parser.add_argument('--settings', type=str, action='append',
                        help='Additional settings in the format NAME=VALUE')

    # Output options
    parser.add_argument('-o', '--output', type=str,
                        help='Output file (e.g., output.json)')
    parser.add_argument('-t', '--output-format', type=str,
                        help='Output format (e.g., json, csv, xml)')

    return parser.parse_args()


def run_spider(spider_class=LinkFollowerSpider, **kwargs):
    """
    Run a spider with the project settings.

    Args:
        spider_class: The spider class to run (default: LinkFollowerSpider)
        **kwargs: Additional keyword arguments to pass to the spider
    """
    # Get the project settings
    settings = get_project_settings()

    # Apply any custom settings
    custom_settings = kwargs.pop('custom_settings', {})
    for name, value in custom_settings.items():
        settings.set(name, value)

    # Configure output if specified
    output_file = kwargs.pop('output_file', None)
    output_format = kwargs.pop('output_format', None)

    if output_file:
        settings.set('FEED_URI', output_file)
        if output_format:
            settings.set('FEED_FORMAT', output_format)

    # Create a crawler process with the project settings
    process = CrawlerProcess(settings)

    # Add the spider to the process with any provided arguments
    process.crawl(spider_class, **kwargs)

    # Start the crawling process
    process.start()


if __name__ == "__main__":
    print("Starting the scraping process...")

    # Parse command line arguments
    args = parse_args()

    # Prepare spider parameters
    spider_params = {}

    # Set start URLs if provided
    if args.start_urls:
        spider_params['start_urls'] = args.start_urls.split(',')

    # Set allowed domains if provided
    if args.allowed_domains:
        spider_params['allowed_domains'] = args.allowed_domains.split(',')

    # Prepare custom settings
    custom_settings = {}
    if args.settings:
        for setting in args.settings:
            name, value = setting.split('=', 1)
            # Try to convert value to appropriate type
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
            custom_settings[name] = value

    spider_params['custom_settings'] = custom_settings

    # Set output options
    if args.output:
        spider_params['output_file'] = args.output
        if args.output_format:
            spider_params['output_format'] = args.output_format

    # Select the spider class
    if args.spider == 'example':
        spider_class = ExampleSpider
    elif args.spider == 'link_follower':
        spider_class = LinkFollowerSpider
    else:
        print(f"Unknown spider: {args.spider}")
        sys.exit(1)

    # Run the selected spider with the provided parameters
    run_spider(spider_class, **spider_params)

    print("Scraping process completed.")
