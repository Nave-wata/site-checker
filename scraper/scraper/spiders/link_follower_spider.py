import scrapy


class LinkFollowerSpider(scrapy.Spider):
    name = "link_follower"
    allowed_domains = ["example.com"]  # Change this to your target domain
    start_urls = ["http://example.com"]  # Change this to your starting URL

    # Custom settings for this spider
    custom_settings = {
        'DEPTH_LIMIT': 10,  # Limit crawl depth to prevent infinite crawling
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter',  # Filter out duplicate requests
    }

    def __init__(self, *args, **kwargs):
        """
        Initialize the spider with custom parameters.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        super(LinkFollowerSpider, self).__init__(*args, **kwargs)

        # Allow overriding start_urls and allowed_domains from command line or entry.py
        if 'start_urls' in kwargs:
            self.start_urls = kwargs.get('start_urls')
        if 'allowed_domains' in kwargs:
            self.allowed_domains = kwargs.get('allowed_domains')

        # Initialize a set to track visited URLs (in addition to Scrapy's built-in duplicate filtering)
        self.visited_urls = set()

    def parse(self, response):
        """
        Parse the response, extract data, and follow links.

        Args:
            response: The response object

        Returns:
            Yields items and requests to follow links
        """
        # Skip if we've already processed this URL (extra safety check)
        if response.url in self.visited_urls:
            return

        # Add URL to visited set
        self.visited_urls.add(response.url)

        # Extract page information
        page_info = {
            'url': response.url,
            'title': response.css('title::text').get(),
            'h1': response.css('h1::text').get(),
            'links': []
        }

        # Extract all <a> tags and their href attributes
        for a_tag in response.css('a'):
            href = a_tag.css('::attr(href)').get()
            text = a_tag.css('::text').get() or ''

            if href:
                # Clean and normalize the href
                href = href.strip()

                # Store link information
                link_info = {
                    'href': href,
                    'text': text.strip()
                }
                page_info['links'].append(link_info)

                # Follow the link if it's not a fragment or external link
                if not href.startswith('#') and not href.startswith('javascript:'):
                    yield response.follow(href, self.parse)

        # Yield the page information
        yield page_info
