import scrapy

class LinksSpider(scrapy.Spider):
    name = 'links_spider'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        # Log the response URL
        self.log(f"Parsing URL: {response.url}")

        # Extract all href attributes from <a> tags
        links = response.css('a::attr(href)').getall()
        self.log(f"Found links: {links}")  # Log found links

        for link in links:
            yield {
                'link': response.urljoin(link)  # Make the link absolute
            }
