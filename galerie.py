# -*- coding: utf-8 -*-
import scrapy


class GalerieSpider(scrapy.Spider):
    galeries = []
    name = 'galerie'
    allowed_domains = ['ensa.uit.ac.ma/galerie/']
    start_urls = ['http://ensa.uit.ac.ma/galerie/']
    all_pages = ""
    counter = 0

    @classmethod
    def getGaleries(cls):
        return cls.galeries

    def parse(self, response):
        print("\033[1;33mCounter = %d\033[0m" % self.counter)
        if (self.all_pages == ""):
            self.all_pages = response.xpath("//*[starts-with(@class, 'block-pagination')]/div[starts-with(@class, 'by_number')]/a/@href").extract()[1:]
        albums = response.xpath("//*[@class='gallery_folder grid_4']")
        for album in albums:
            album_link = album.xpath(".//a/@href").extract_first() or ""
            album_name = album.xpath(".//a[@class='album_name']/text()").extract_first() or ""
            album_photo = album.xpath(".//a/img/@src").extract_first() or ""
            album_photos_number = album.xpath(".//*[starts-with(@class, 'counter')]/text()").extract_first().strip() or ""

            self.galeries.append({
                "album_link": album_link,
                "album_name": album_name,
                "album_photo": album_photo,
                "album_photos_number": album_photos_number
            })

        next_page = self.all_pages[self.counter]
        self.counter += 1
        print("\n")
        print("\033[1;33mCrawling : {}".format(next_page))
        print("\033[1;33mAll pages : {}".format(self.all_pages))
        print("\n")
        print("\033[0m")

        yield scrapy.Request(next_page)




