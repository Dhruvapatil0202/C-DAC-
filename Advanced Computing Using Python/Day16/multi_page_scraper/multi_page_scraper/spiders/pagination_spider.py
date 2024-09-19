import scrapy


class BooksSpider(scrapy.Spider):
    name = 'multiPageSpider'  #singlePageSpider
    start_urls = ['https://books.toscrape.com/catalogue/category/books/mystery_3/index.html']

    def parse(self, response):
        #Extract h1 title of the page
        page_title = response.css('h1::text').get()
        # Print the page title of the page
        print(f"Page Title: {page_title}")
        #Extract book information


        for book in response.css('article.product_pod').getall():
            print(book)

            title = book.css('h3 a::attr(title)').get()
            url = book.css('h3 a::attr(href)').get()
            # Yield book data along with the page
            yield {
                'page_title' : page_title, # add the page title to each entry
                'title': title,
                'url' : response.urljoin(url)
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)