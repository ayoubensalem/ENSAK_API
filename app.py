# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api
from flask_caching import Cache
from news import NewsSpider
from galerie import GalerieSpider
from article import ArticleSpider
from gallery import GallerySpider
import scrapy.crawler as crawler
from multiprocessing import Process, Queue
from twisted.internet import reactor
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

class News(Resource):
    @cache.cached(timeout=600)
    def get(self):
        data = []
        def f(q):
            try:
                runner = crawler.CrawlerRunner()
                deferred = runner.crawl(NewsSpider)
                deferred.addBoth(lambda _: reactor.stop())
                reactor.run()
                q.put(NewsSpider.getNews())
            except Exception as e:
                q.put(e)

        q = Queue()
        p = Process(target=f, args=(q,))
        p.start()
        result = q.get()
        p.join()
        return {'news': result}


class Galleries(Resource):
    @cache.cached(timeout=600)
    def get(self):
        data = []
        def f(q):
            try:
                runner = crawler.CrawlerRunner()
                deferred = runner.crawl(GalerieSpider)
                deferred.addBoth(lambda _: reactor.stop())
                reactor.run()
                q.put(GalerieSpider.getGaleries())
            except Exception as e:
                q.put(e)

        q = Queue()
        p = Process(target=f, args=(q,))
        p.start()
        result = q.get()
        p.join()
        return {'galeries': result}

class Article(Resource):
    def get(self, name):
        ArticleSpider.start_urls = ['http://ensa.uit.ac.ma/{}'.format(name)]
        data = []
        def f(q):
            try:
                runner = crawler.CrawlerRunner()
                deferred = runner.crawl(ArticleSpider)
                deferred.addBoth(lambda _: reactor.stop())
                reactor.run()
                q.put(ArticleSpider.getArticle())
            except Exception as e:
                q.put(e)

        q = Queue()
        p = Process(target=f, args=(q,))
        p.start()
        result = q.get()
        p.join()
        return result

class Gallery(Resource):
    def get(self, name):
        GallerySpider.start_urls = ['http://ensa.uit.ac.ma/gallerie/{}'.format(name)]
        data = []
        def f(q):
            try:
                runner = crawler.CrawlerRunner()
                deferred = runner.crawl(GallerySpider)
                deferred.addBoth(lambda _: reactor.stop())
                reactor.run()
                q.put(GallerySpider.getGallery())
            except Exception as e:
                q.put(e)

        q = Queue()
        p = Process(target=f, args=(q,))
        p.start()
        result = q.get()
        p.join()
        return {'images': result}





api.add_resource(News, '/articles')
api.add_resource(Article, '/articles/<name>')
api.add_resource(Galleries, '/galleries')
api.add_resource(Gallery, '/galleries/<name>')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
