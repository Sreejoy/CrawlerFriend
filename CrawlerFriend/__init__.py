"""
If you have some interest on a topic and you visit same 2-3 websites
 and search for some keywords. CrawlerFriend can help you filter those
 things and can reduce your browsing time.

CrawlerFriend is a light-weight, pluggable, easy to use web crawler and scrapper.
Given a list of website links and your preferable keywords, you can
get the crawling result in any format. Also you can view the searched
content on a web browser.
"""

__author__ = "Sreejoy Halder (sreejoy4242@gmail.com)"
__version__ = "1.0.8"
__copyright__ = "Copyright (c) 2018 Sreejoy Halder"
__license__ = "MIT"

import webbrowser,requests,Queue
from bs4 import BeautifulSoup

class Crawler():
    """
        This class defines the basic crawler given the website links,
        keywords and target HTML tags.
    """
    max_links = 50
    all_data = {}
    inspected_tags = ['title', 'h1', 'h2', 'h3']
    all_links = Queue.Queue()
    visited_links = set()
    key_words = []

    def __init__(self,urls,keywords,max_link_limit=50,tags=None):
        """

        :param urls: The URL(s) from where the crawling will begin. Can be a string(single URL) or a list of URLs.
        :param keywords: The keyword(s) which will be looked for in tags and links during crawling. Can be a
        string(single keyword) or a list of keywords.
        :param max_link_limit: The maximum number of link parsed by Crawler. By default the value is 50.
        :param tags: The tag(s) which will be looked for in HTML files during crawling. Can be a
        string(single tag) or a list of tags. If not specified, by default, its a list containing 4 tags('title','h1','h2','h3').
        """
        try:
            if type(urls) is list:
                if len(urls) == 0:
                    raise ValueError("urls parameter can't an empty list")
                else:
                    self.base_urls = urls
            elif type(urls) is str:
                self.base_urls = [urls]
            else:
                raise TypeError("urls parameter must be a list or a string")

            if type(keywords) is list:
                if len(keywords) == 0:
                    raise ValueError("keywords parameter can't an empty list")
                else:
                    self.key_words = keywords
            elif type(keywords) is str:
                self.key_words = [keywords]
            else:
                raise TypeError("keywords parameter must be a list or a string")

            if tags:
                if type(tags) is list:
                    if len(tags) == 0:
                        raise ValueError("tags parameter can't an empty list")
                    else:
                        self.inspected_tags = tags
                elif type(tags) is str:
                    self.inspected_tags = [tags]
                else:
                    raise TypeError("tags parameter must be a list or a string")

            if type(max_link_limit) is int:
                self.max_links = max_link_limit
            elif type(max_link_limit) is str:
                self.max_links = int(max_link_limit)
            else:
                raise TypeError("max_link_limit parameter must be an int or a string of an int")

            for each in self.key_words:
                self.all_data[each] = {}
        except Exception, e:
            print e
            return

    def _check_for_keywords(self,link, url=False):
        """
        check if a text or a URL matches with any of the predefined keywords
        :param link: a text or a URL
        :param url: if link is an URL
        :return: bool,matching keyword
        """
        if not link:
            return False, ""
        link = link.encode("utf8")
        for each in self.key_words:
            if url:
                if str(each).strip().lower().replace(' ', '+') in link or \
                                str(each).strip().lower().replace(' ', '-') in link:
                    return True, each
            else:
                if str(each).strip().lower() in str(link).strip().lower():
                    return True, each
        return False, ""

    def _add_new_links(self,url):
        """
        Given a URL it will inspect the HTML of the URL and find for user defined tags and all the links.
        Then it will inspect of the text of those tags or links contain any user defined keywords.
        If a text contains keywords then this URL will be added in the results. If a link contains
        keywords then that link will be added in the results plus that link will be saved in a queue
        so that the crawler can crawl it further.
        :param url: base URL
        :return: None
        """
        try:
            print "Visiting:%s" % url
            self.visited_links.add(url)
            html_result = requests.get(url,verify=False)
            content = html_result.text
            html = BeautifulSoup(content, "html.parser")

            for tag in self.inspected_tags:
                for data in html.find_all(tag):
                    text = data.string
                    result, key = self._check_for_keywords(text)
                    if result:
                        self.all_data[key][text] = url

            for link in html.find_all("a"):
                link = link.get('href')
                if not link: continue
                result, key = self._check_for_keywords(link, True)
                if link not in self.visited_links and result:
                    self.all_links.put(link)
        except Exception, e:
            print e
            return

    def _put_all_base_urls_to_queue(self):
        """
        puts all user defined URLs to the Queue from where crawler picks up a URL, crawl, add relevant
        URLs and repeat.
        :return: None
        """
        for url in self.base_urls:
            self.all_links.put(url)

    def crawl(self):
        """
        Crawler picks up a URL, crawl, add relevant URLs and repeat. Will stop os Queue is empty or
        no of URL visited is equal to the maximum link limit.
        :return: None
        """
        self._put_all_base_urls_to_queue()

        while not self.all_links.empty() and len(self.visited_links) < self.max_links:
            link = self.all_links.get()
            if link not in self.visited_links:
                self._add_new_links(link)

    def get_result_in_html(self):
        """
        Will write all the result in a HTML file name 'output.html'. And will open the html file
        in web browser using webdriver method.
        :return: None
        """
        html = """
            <html>
                <head>
                    <title>CrawlerFriend</title>
                </head>
                <body>
                    <h1 align='center'>CrawlerFriend</h1>
        """
        for key in self.all_data.keys():
            if len(self.all_data[key]) == 0:
                continue
            html += """<h4>%s(%d search result found)</h4>""" % (key, len(self.all_data[key]))
            html += """<ol>"""
            for elem in self.all_data[key].keys():
                link = elem.encode("utf8")
                headline = self.all_data[key][elem].encode("utf8")
                html += """<li><a href='%s' target='_blank'>%s</a></li>""" % (headline, link)

            html += """</ol>"""

        html += """
                </body>
            </html>
        """

        with open('output.html', 'w') as f:
            f.write(html)

        webbrowser.open('output.html')


    def get_result_of_keyword_in_html(self,key):
        """
        Will write all the result of a keyword in a HTML file name 'output.html'. And will open the html file
        in web browser using webdriver method.
        :return: None
        """
        html = """
            <html>
                <head>
                    <title>CrawlerFriend</title>
                </head>
                <body>
                    <h1 align='center'>CrawlerFriend</h1>
        """
        if key not in self.key_words:
            return ValueError("'%s' is not a predefined keyword" % key)

        html += """<h4>%s(%d search result found)</h4>""" % (key, len(self.all_data[key]))
        html += """<ol>"""
        for elem in self.all_data[key].keys():
            link = elem.encode("utf8")
            headline = self.all_data[key][elem].encode("utf8")
            html += """<li><a href='%s' target='_blank'>%s</a></li>""" % (headline, link)

        html += """</ol>"""

        html += """
                </body>
            </html>
        """

        with open('output.html', 'w') as f:
            f.write(html)

        webbrowser.open('output.html')


    def get_result(self):
        """
        it will return the search result in a Dictionary
        :return: A Dictionary which contains the search result
        """
        return self.all_data


    def get_result_of_keyword(self,key):
        """
        Given a keyword it will return the search result in a Dictionary
        :param key: The keyword that user want to get the result of
        :return: A Dictionary which contains the search results
        """
        if key in self.key_words:
            return self.all_data[key]
        else:
            return ValueError("'%s' is not a predefined keyword"%key)

if __name__ == '__main__':
    crawler = Crawler(["URL1","URL2"],["Keyword1","Keyword2"])
    crawler.crawl()
    crawler.get_result_in_html()