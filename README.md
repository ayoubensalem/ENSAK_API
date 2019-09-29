# ENSAK API 

A simple API under construction for a mobile application : https://github.com/ayoubensalem/ENSAKenitra , using FLASK-RESTful and Scrapy framework.

Entry file : **app.py** where all the resources are defined.

Scrapy Spiders : 
 * Articles : *articles.py*
 * Galleries : *galleries.py*
 * Article : *article.py*
 * Gallerie : *gallerie.py*

Flask-Cache is used for caching response  :
 - Type : simple ( You can use redis server, for more info check the docs. ) 
 - timeout = 600 seconds

---
*BASE_URL* : https://ensak-api.herokuapp.com
---

> Endpoints : 
 - /
 - /articles
 - /articles/{:name}
 - /galleries
 - /galleries/{:name}

--- 
Dependencies :

`pip install -r requirements.txt`
