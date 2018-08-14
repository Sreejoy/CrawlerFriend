## CrawlerFriend

A light weight **Web Crawler** that supports **Python 2.7** which gives search results in HTML form or in
Dictionary form given URLs and Keywords. If you regularly visit a few websites and look for a few keywords
then this python package will automate the task for you and
return the result in a HTML file in your web browser.

### Installation
```
pip install CrawlerFriend
```

### How to use?
#####All Result in HTML
```
import CrawlerFriend

urls = ["http://www.goal.com/","http://www.skysports.com/football","https://www.bbc.com/sport/football"]
keywords = ["Ronaldo","Liverpool","Salah","Real Madrid","Arsenal","Chelsea","Man United","Man City"]

crawler = CrawlerFriend.Crawler(urls, keywords)
crawler.crawl()
crawler.get_result_in_html()
```

This code will return the following result:

![](https://i.imgur.com/xXJyjoX.png)

##### All Result in Dictionary
```
result_dict = crawler.get_result()
```

##### Changing Default Arguments
CrawlerFriend uses four HTML tags 'title', 'h1', 'h2', 'h3' and max_link_limit = 50 by default for searching.
But it can be changed by passing arguments to the constructor:
 ```
crawler = CrawlerFriend.Crawler(urls, keywords, max_link_limit=200, tags=['p','h4'])
crawler.crawl()
```

