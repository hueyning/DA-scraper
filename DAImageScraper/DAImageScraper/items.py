# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # direct link to image file for downloading via ImagePipeline
    image_urls = scrapy.Field()

    # link to specific image page for scraping more stats
    page_links = scrapy.Field()

    # image attributes
    titles = scrapy.Field()  # image title
    date_posted = scrapy.Field()  # date posted
    hashtags = scrapy.Field()  # hashtags

    # image stats
    faves = scrapy.Field()  # number of faves of the current image
    comments = scrapy.Field()  # number of comments of the current image
    views = scrapy.Field()  # number of views of the current image

    # artist details
    artists = scrapy.Field()  # artist's name
    artist_urls = scrapy.Field()  # link to the artist's account
    artist_page_views = scrapy.Field()  # number of total page views
    artist_deviations = scrapy.Field()  # number of images posted by the artist
    artist_watchers = scrapy.Field()  # number of accounts following the artist
    artist_watching = scrapy.Field()  # number of accounts the artist is following
    artist_favourites = scrapy.Field()  # number of total faves received
    artist_comments_made = scrapy.Field()  # number of comments made
    artist_comments_received = scrapy.Field()  # number of total comments received

    artist_account_age = scrapy.Field()  # account age

    # to be filled in by ImagePipeline
    image_paths = scrapy.Field()  # location of image in local storageages = scrapy.Field()
