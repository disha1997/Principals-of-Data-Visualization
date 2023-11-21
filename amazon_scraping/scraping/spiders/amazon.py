import scrapy
from scraping.items import ScrapingItem

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = [
    f'https://www.amazon.in/s?k=iphone&i=electronics&rh=n%3A1389401031&page={i}&qid=1696175614&ref=sr_pg_{i}'
    for i in range(2, 7)]


    def parse(self, response):
        phone_item = ScrapingItem()
        products = response.xpath('//div[@data-component-type="s-search-result"]')

        for product in products:
            name = product.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()').get()
            rating = product.xpath('.//span[@class="a-icon-alt"]/text()').get()
            price = product.xpath('.//span[@class="a-price-whole"]/text()').get()
            

            if 'Apple iPhone' in name:  
                phone_item['name'] = name
                phone_item['rating'] = rating
                phone_item['price'] = price
                
                yield {
                'name': name,
                'rating': rating,
                'price': price }

     
