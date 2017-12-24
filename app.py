# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from flask import Flask
from flask_restful import Resource, Api
from news import NewsSpider
from galerie import GalerieSpider
import json
import scrapy.crawler as crawler
from multiprocessing import Process, Queue
from twisted.internet import reactor


app = Flask(__name__)
api = Api(app)

class News(Resource):
    def get(self):
        runner = CrawlerRunner()
        d = runner.crawl(NewsSpider)
        d.addBoth(lambda _: reactor.stop())
        reactor.run()
        # process = CrawlerProcess({
        #     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        # })
        # process.crawl(NewsSpider)
        # process.start()
        return {'news': NewsSpider.getNews() }


class Galerie(Resource):
    def get(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(GalerieSpider)
        process.start()
        return {'galeries': GalerieSpider.getGaleries()}



api.add_resource(News, '/news')
api.add_resource(Galerie, '/galerie')

if __name__ == '__main__':
    app.run(port=5000)
