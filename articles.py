# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['ensa.uit.ac.ma']
    start_urls = ['http://ensa.uit.ac.ma/category/actualites/']
    first_time = True
    news_list = []


    @classmethod
    def getNews(cls):
        return cls.news_list

    def parse(self, response):
        posts = response.xpath("//*[@id='post']")
        for post in posts:
            image = post.xpath(".//a/img/@src").extract_first().strip()
            link = post.xpath(".//a/@href").extract_first().strip()
            title = post.xpath(".//*[@class='block-content']/a/h1/text()").extract_first().strip()
            description = post.xpath(".//*[@class='block-content']/div[@class='description']/text()").extract_first().strip()
            self.news_list.append({
                "image": image,
                "link": link,
                "title": title,
                "description": description
            })

        next_page = response.xpath("//*[@class='by_arrows alignright']/a/@href").extract()
        if (len(next_page) > 1 or self.first_time) :
            self.first_time = False
            next_page = next_page[-1]
            yield scrapy.Request(next_page)
            print("\n\033[1;33mDebug : {}\n".format(next_page))
            print("\033[0m")








