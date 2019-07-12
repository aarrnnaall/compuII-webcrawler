import sqlite3  
import urllib2 
import requests
from urlparse import urlparse
<<<<<<< HEAD
from parseo import html
=======
from HTMLParser import HTMLParser
from parseo import MyHTMLParser
from bs4 import BeautifulSoup
import mysql.connector
>>>>>>> 644e6bcdb01667438ab7ce2e55eb849e12d47fd2

class HREFParser(HTMLParser):
    """
    Parser that extracts hrefs
    """
    hrefs = set()
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            dict_attrs = dict(attrs)
            if dict_attrs.get('href'):
                self.hrefs.add(dict_attrs['href'])


def get_local_links(html, domain):
    """
    Read through HTML content and returns a tuple of links
    internal to the given domain
    """
    hrefs = set()
    parser = HREFParser()
    parser.feed(html)
    for href in parser.hrefs:
        u_parse = urlparse(href)
        if href.startswith('/'):
            # purposefully using path, no query, no hash
            hrefs.add(u_parse.path)
        else:
          # only keep the local urls
          if u_parse.netloc == domain:
            hrefs.add(u_parse.path)
    return hrefs

class Crawler(object):  
    def __init__(self, cache=None, depth=2):
        """
        depth: how many time it will bounce from page one (optional)
        cache: a basic cache controller (optional)
        """
        self.depth = depth
        self.content = {}
        self.cache = cache

    def crawl(self, url, no_cache=None):
        """
        url: where we start crawling, should be a complete URL like
        'http://www.intel.com/news/'
        no_cache: function returning True if the url should be refreshed
        """
        u_parse = urlparse(url)
        self.domain = u_parse.netloc
        self.content[self.domain] = {}
        self.scheme = u_parse.scheme
        self.no_cache = no_cache
        self._crawl([u_parse.path], self.depth)

    def set(self, url, html):
        self.content[self.domain][url] = html
        if self.is_cacheable(url):
            self.cache.set(self.domain, url, html)

    def get(self, url):
        page = None
        if self.is_cacheable(url):
          page = self.cache.get(self.domain, url)
        if page is None:
          page = self.curl(url)
        else:
          print "cached url... [%s] %s" % (self.domain, url)
        return page

    def is_cacheable(self, url):
        return self.cache and self.no_cache \
            and not self.no_cache(url)

    def _crawl(self, urls, max_depth):
        n_urls = set()
        if max_depth:
            for url in urls:
                # do not crawl twice the same page
                if url not in self.content:
                    html = self.get(url)
                    self.set(url, html)
                    n_urls = n_urls.union(get_local_links(html, self.domain))
            self._crawl(n_urls, max_depth-1)

    def execute_query(self,url,titulo,descripcion):

        Host='127.0.0.1'
        usuario='root'
        password='root'
        db_name='crawler'
        query =''
        datos=(Host,usuario,password,db_name)
        conn=MySQLdb.connect(*datos)
        cursor=conn.cursor()
        cursor.execute(query)

        if query.upper().startTswitch('SELECT'):
            data= cursor.fetchall()
        else:
            conn.comit()
            data=None

        cursor.close()
        conn.close()

        return data

        dato=(titulo,url,descripcion)
        query="INSERT INTO auto (titulo,url,desc) VALUES('%s','%s','%s')"%dato

        execute_query()


    def curl(self, url):
        """
        return content at url.
        return empty string if response raise an HTTPError (not found, 500...)
        """
        try:
            #print "retrieving url... [%s] %s" % (self.domain, url)
            
            print("___________________________________Url__________________________________________________")
            print (self.domain + url)
            #url = self.domain + url
            req = requests.get("https://"+self.domain+url)
            soup = BeautifulSoup(req.text, "lxml") 
            desc = soup.findAll('meta',attrs={'name':'description'})                
            print("___________________________________Titulo_______________________________________________")
            #title = soup.title.string
            print(soup.title.string)
            print("___________________________________Descripcion__________________________________________")
            for desc in desc:
                #desc_cont = desc.get('content')
                print(desc.get('content'))
            
                
            #self.execute_query(self.domain+url,soup.title.string,desc.get('content'))
            req = urllib2.Request('%s://%s%s' % (self.scheme, self.domain, url))
            response = urllib2.urlopen(req)
            #print(response.read().decode('ascii','ignore'))
            return response.read().decode('ascii', 'ignore')
        except urllib2.HTTPError, e:
            print "error [%s] %s: %s" % (self.domain, url, e)
            return ''
