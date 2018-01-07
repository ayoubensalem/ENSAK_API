# -*- coding: utf-8 -*-
import scrapy


class GallerySpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['ensa.uit.ac.ma']
    start_urls = []
    images = []

    # def __init__(self, article_name=None,*args, **kwargs):
    #     super(ArticleSpider, self).__init__(*args, **kwargs)
    #     self.start_urls = ['http://ensa.uit.ac.ma/{}'.format(article_name)]

    @classmethod
    def getGallery(cls):
        return cls.images

    def parse(self, response):
        print("\033[1;33mStart Crawling\033[0m")
        results = response.xpath("//div[@id='more_content']/div[@class='grid_2 album_image']/a/img/@src").extract()
        for image in results:
            self.images.append(image)
        print("\033[1;33m Images {} \033[0m".format(results))











