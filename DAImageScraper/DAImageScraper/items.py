# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ImageItem(scrapy.Item):

    # scrape from site
    image_urls = scrapy.Field()
    artists = scrapy.Field()
    faves = scrapy.Field()
    comments = scrapy.Field()
    
    # to be returned
    image_paths = scrapy.Field()
    images = scrapy.Field()