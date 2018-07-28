## CrawlerFriend

A light weight **Web Crawler** that supports **Python 2.7** which gives search results in **HTML form** or in 
**Dictionary** form given **URLs** and **Keywords**. If you regularly visit a few websites and look for a few keywords
(For example, looking for certain team/players in sports website, looking for a bunch of topics on a website...), 
then this python package (which is a friend of you and a crawler by nature) will automate the task for you and 
return the result in a **HTML** file in your **web browser**.

### Installation
```
pip install CrawlerFriend
```

### Start the Crawler
#### Import Module
```
import CrawlerFriend
```
#### Start the Crawler
How to start the Crawler? Crawler takes 4 Arguments:
1. urls (List of URLs)
2. keywords (List of Keywords) 
3. max_link_limit [Optional] (Maximum no. of link that will be visited, By Default its value is 50)
4. tags [Optional] (The HTML tags that the Crawler will search for,By Default its value is ['title', 'h1', 'h2', 'h3'])

```
crawler = CrawlerFriend.Crawler(["https://Website1.com/", "http://Website2.com/"], ["Keyword1", "Keyword2"])
crawler.crawl()
```

### Get Search Results
There are several ways to get the search results(all or for a keyword) in HTML or in Dictionary form
#### All Result in HTML
```
crawler.get_result_in_html()
```

#### All Result in Dictionary
```
result_dict = crawler.get_result()
```

#### Result of a Keyword in HTML
```
crawler.get_result_of_keyword_in_html()
```

#### Result of a Keyword in Dictionary
```
result_dict = crawler.get_result_of_keyword('keyword1')
```

### Specify Max Link Limit
CrawlerFriend uses 50 as max_link_limit by default for searching. 
But users can use their own max_link_limit as well like this:
 ```
crawler = CrawlerFriend.Crawler(["https://Website1.com/", "http://Website2.com/"], ["Keyword1", "Keyword2"], max_link_limit=200)
crawler.crawl()
```

### Specify tags
CrawlerFriend uses four HTML tags 'title', 'h1', 'h2', 'h3' by default for searching. 
But users can use their own tags as well like this:
 ```
crawler = CrawlerFriend.Crawler(["https://Website1.com/", "http://Website2.com/"], ["Keyword1","Keyword2"], tags=['p','h4'])
crawler.crawl()
```
