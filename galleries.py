# -*- coding: utf-8 -*-
import scrapy
from flask import jsonify

class GalerieSpider(scrapy.Spider):
    name = 'galleries'
    allowed_domains = ['ensa.uit.ac.ma/galerie/']
    start_urls = ['http://ensa.uit.ac.ma/galerie/']
    counter = 0
    galeries = []

    @classmethod
    def getGaleries(cls):
        print("\033[1;33mHere getGaleris\033[0m")
        return cls.galeries

    def parse(self, response):

        print("\033[1;33mStart Crawling\033[0m")
        albums = response.xpath("//*[@class='gallery_folder grid_4']")
        for album in albums:
            album_link = album.xpath(".//a/@href").extract_first()
            album_name = album.xpath(".//a[@class='album_name']/text()").extract_first()
            album_photo = album.xpath(".//a/img/@src").extract_first()
            album_photos_number = album.xpath(".//*[starts-with(@class, 'counter')]/text()").extract_first().strip()

            self.galeries.append({
                "album_link": album_link,
                "album_name": album_name,
                "album_photo": album_photo,
                "album_photos_number": album_photos_number
            })
            # all_pages = response.xpath("//div[@class='block-pagination grid_12 alignright']/div[@class='by_number alignleft']/a").extract()
            # all_pages_hrefs = response.xpath("//div[@class='block-pagination grid_12 alignright']/div[@class='by_number alignleft']/a/@href").extract()

            # print("\033[1;33mall_pages\033[0m {}".format(all_pages_hrefs))
            # for i, page in enumerate(all_pages):
            #     if 'active' in page.replace('"', " ").split() and i < len(all_pages):
            #         next_page = all_pages_hrefs[i+1]
            #         print("\033[1;33mNext Page\033[0m {}".format(next_page))
            #         break
            #yield scrapy.Request(next_page)






