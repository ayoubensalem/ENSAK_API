# ENSAK API 

A simple API under construction, using FLASK-RESTful and Scrapy framework.

Entry file : **app.py** where all the resources are defined.
Scrapy Spiders : 
 * news : *news.py*
 * galerie : *galerie.py*

Flask-Cache is used for caching requests :
 - Type : simple ( You can use redis server, for more info check the docs. ) 
 - timeout = 600 seconds

---
*BASE_URL* : https://ensak-api.herokuapp.com
---

> Endpoints : 
 - /news
 - /galerie
