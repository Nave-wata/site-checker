#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Entry point for running the scraper.
This script can be executed directly to run the scraping process.
"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.example_spider import ExampleSpider


def run_spider():
    """
    Run the example spider with the project settings.
    """
    # Get the project settings
    settings = get_project_settings()

    # Create a crawler process with the project settings
    process = CrawlerProcess(settings)

    # Add the example spider to the process
    process.crawl(ExampleSpider)

    # Start the crawling process
    process.start()


if __name__ == "__main__":
    print("Starting the scraping process...")
    run_spider()
    print("Scraping process completed.")
