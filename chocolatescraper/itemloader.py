
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import TakeFirst, MapCompose, Join 

# class chocolateProductItemLoader(ItemLoader):
#   default_output_processor = TakeFirst()
#   price_in = MapCompose(lambda x: x.split('£')[-1])
#   url_in = MapCompose(lambda x: 'https://www.chocolate.co.uk' + x)
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity


class ChocolateProductLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: x.split('£')[-1])
    url_in = MapCompose(lambda x: 'https://www.chocolate.co.uk' + x)
