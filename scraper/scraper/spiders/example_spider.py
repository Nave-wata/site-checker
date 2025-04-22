import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com"]

    def parse(self, response):
        """
        Parse the response and extract data.
        
        Args:
            response: The response object
            
        Returns:
            Yields items or requests
        """
        # Example of extracting data
        yield {
            'title': response.css('title::text').get(),
            'h1': response.css('h1::text').get(),
            'p': response.css('p::text').get(),
        }
