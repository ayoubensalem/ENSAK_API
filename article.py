# -*- coding: utf-8 -*-
import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['ensa.uit.ac.ma']
    start_urls = []
    article = {}

    # def __init__(self, article_name=None,*args, **kwargs):
    #     super(ArticleSpider, self).__init__(*args, **kwargs)
    #     self.start_urls = ['http://ensa.uit.ac.ma/{}'.format(article_name)]

    @classmethod
    def getArticle(cls):
        return cls.article

    def parse(self, response):

        print("\033[1;33mStarting\033[0m")
        title = response.xpath("//h1[@class='title']/text()").extract_first().strip()
        body = response.xpath("//div[@class='post-content']/p").extract()
        body = "\n".join(body)
        print("\033[1;33mCrawling : {}".format(self.start_urls[0]))
        self.article["title"] = title
        self.article["body"] = body








