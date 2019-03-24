import scrapy
from scrapy.pipelines.images import ImagesPipeline
from DAImageScraper.items import ImageItem

class ImageSpider(scrapy.Spider):
    
    name = 'images'
    
    start_urls = ['https://www.deviantart.com/popular-all-time/?q=sherlock']
    

    def parse(self, response):
        
        #get page body
        page = response.css('div.page-results span.thumb')
        
        for img in page:
            
            #initialize image object
            image = ImageItem()
        
            #assign image attributes
            image["image_urls"] = [img.css('::attr(data-super-img)').get()]
            image["faves"] = img.css('span.info span.extra-info span.stats span.faves::text').get()
            image["comments"] = img.css('span.info span.extra-info span.stats span.comments::text').get()
            image["artists"] = img.css('span.info span.extra-info span.artist a img.avatar::attr(title)').get()
        
            if image["image_urls"][0] != None: yield image
        