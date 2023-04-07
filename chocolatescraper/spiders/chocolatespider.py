import scrapy
from typing import List
# import attr 
import attrs


from chocolatescraper.itemloader import ChocolateProductLoader
from chocolatescraper.items import ChocolateProduct

class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response: scrapy.http.Response) -> List[scrapy.Request]:
        products = response.css('product-item')
        for product in products:
            
            chocolate = ChocolateProductLoader(
                item=ChocolateProduct(), selector=product)
            
            chocolate.add_css('name', 'a.product-item-meta__title::text')
            chocolate.add_css('price', 'span.price::text', re=r'([£$€]\d+(?:\.\d{2})?)')
            chocolate.add_css('url', 'div.product-item-meta a::attr(href)')
            yield chocolate.load_item()
            # yield{
            #     'name':  product.css('a.product-item-meta__title::text').get(),
            #     'price':  product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>', '').replace('</span>', ''),
            #     'url':  'https://www.chocolate.co.uk' + product.css('div.product-item-meta a::attr(href)').get(),
            # }
        next_page = response.css("[rel='next']::attr(href)").get()
        # print(next_page)
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)
        
