# DA-scraper

DeviantArt Image Scraper

<hr>

Webscraper for scraping https://www.deviantart.com/ using Python's Scrapy module. The scraper is available in two formats:

- Jupyter notebook 
- Scrapy-framework scraper 

Both versions are fully-functional, which one to use is up to personal preference.

Outputs:
- Images in DA-images folder. DA-images folder must be initialized for images to be downloaded and stored. Folder name can be changed, but IMAGE_STORE must be changed in scraper settings as well.
- Image data (faves, comments, artist) in 'image-data.json'.

To-do:
- Implement "next page" feature in scraper.
- Edit start_urls - should be more robust.
- Implement delay timer.



