import scrapy
from DAImageScraper.items import ImageItem


class ImageSpider(scrapy.Spider):
    name = 'image-spider'

    start_urls = [
        'https://www.deviantart.com/search/deviations/visual-art/original-work/digital-art?limit=60&order=popular-all-time&page=0&q=cyberpunk', # max page limit is 60 for some reason
    ]

    # initialize page at 0
    page = 0
    # set page limit to control the amount of images downloaded
    page_limit = 100
    # number of images found
    img_count = 0


    def parse(self, response):

        self.logger.info(f'Scraping {response.url}')

        # get list of image links from the page
        img_links = response.css('div[class=_2tv7Y] a[data-hook="deviation_link"]::attr(href)').getall()
        self.logger.info(f'Found {len(img_links)} images on page')
        self.img_count += len(img_links)

        for link in img_links:
            yield scrapy.Request(link, callback=self.parse_image)

        # go to next page
        while self.page < self.page_limit:
            self.page += 1  # increment page by 1
            next_page = f'https://www.deviantart.com/search/deviations/visual-art/original-work/digital-art?limit=60&order=popular-all-time&page={self.page}&q=cyberpunk'
            yield scrapy.Request(next_page, callback=self.parse)

        self.logger.info(f'Total images parsed should be {self.img_count} images.')

    def parse_image(self, response):

        self.logger.info(f'Scraping image: {response.url}')

        # initialize image item
        image = ImageItem()

        # get image url (for downloading via ImagePipeline)
        image["image_urls"] = [response.css('div[data-hook="art_stage"] img::attr(src)').get()]
        # get other image info
        image["page_links"] = response.url
        image['titles'] = response.css('div[class="_3qGVQ"]::text').get()
        image['date_posted'] = response.css('div[class="_3XxFW"]::text').getall()[-1]

        # check whether image has hashtags (some don't)
        hashtag = response.css('div[class="_2ogLQ"] span::text').getall()
        if hashtag: image['hashtags'] = hashtag

        # get image stats
        stats = response.css('div[class="hYJJ_"] span::text').getall()

        # remove blanks from list and limit to first 3 items (4th item onwards is irrelevant)
        stats = ''.join(stats).split()[:3]

        # the responses are ordered in: faves, comments, views
        image['faves'] = stats[0]
        image['comments'] = stats[1]
        image['views'] = stats[2]

        yield image
        # get artist info
        artist_name = response.css('a[data-hook="user_link"]::attr(title)').get()

        #if artist_name:
        #    image['artists'] = response.css('a[data-hook="user_link"]::attr(title)').get()
        #    artist_gallery = response.css('a[data-hook="user_link"]::attr(href)').get()
        #    image['artist_urls'] = artist_gallery.replace('gallery', 'about')  # replace the /gallery pointer to /about
        #    request = scrapy.Request(image['artist_urls'], callback=self.parse_artist, meta={'image': image})
        #    yield request
        #else:  # if no artist name (sometimes artists are banned), just yield the image
        #    image['artists'] = 'Banned'
        #    yield image

    def parse_artist(self, response):

        # get image item for the higher-level parser
        image = response.meta['image']

        # get stat data
        artist_stats = response.css('div[class="_1loOw"]::text').getall()

        # get stat headers
        headers = response.css('div[class="_1loOw"] span::text').getall()
        # prefix 'artist', lowercase, and replace blank space with underscore to make headers neat
        headers = ['artist_' + s.lower().replace(' ', '_') for s in headers]

        # assign stats to headers
        for i in range(len(artist_stats)):
            image[headers[i]] = artist_stats[i]

        # get artist personal info
        personal_info = response.css('div[class="_2B4Yo _3N4ed"] span::text').getall()
        image['artist_account_age'] = personal_info[-1]

        return image