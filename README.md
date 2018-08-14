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
```
import CrawlerFriend

urls = ["http://www.goal.com/","http://www.skysports.com/football","https://www.bbc.com/sport/football"]
keywords = ["Ronaldo","Liverpool","Salah","Real Madrid","Arsenal","Chelsea","Man United","Man City"]

crawler = CrawlerFriend.Crawler(urls, keywords)
crawler.crawl()
crawler.get_result_in_html()
```

#### Get Search Results in Different Ways
##### All Result in HTML
```
crawler.get_result_in_html()
```

##### All Result in Dictionary
```
result_dict = crawler.get_result()
```

##### Result of a Keyword in HTML
```
crawler.get_result_of_keyword_in_html()
```

##### Result of a Keyword in Dictionary
```
result_dict = crawler.get_result_of_keyword('Liverpool')
```

##### Specify Max Link Limit
CrawlerFriend uses 50 as max_link_limit by default for searching. 
But users can use their own max_link_limit as well like this:
 ```
crawler = CrawlerFriend.Crawler(urls, keywords,max_link_limit=200)
crawler.crawl()
```

##### Specify tags
CrawlerFriend uses four HTML tags 'title', 'h1', 'h2', 'h3' by default for searching. 
But users can use their own tags as well like this:
 ```
crawler = CrawlerFriend.Crawler(urls, keywords, tags=['p','h4'])
crawler.crawl()
```
