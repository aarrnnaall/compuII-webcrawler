import threading, urllib, urlparse
from HTMLParser import HTMLParser
import sys


class LinkHTMLParser(HTMLParser):
    A_TAG = "a"
    HREF_ATTRIBUTE = "href"

    def __init__(self):
        self.links = []
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
<<<<<<< HEAD
        if cmp(tag, self.A_TAG) == 0:
            for (key, value) in attrs:
                if cmp(key, self.HREF_ATTRIBUTE) == 0:
                    print("\t" + value)
=======
        """Add all 'href' links within 'a' tags to self.links"""
        if cmp(tag, self.A_TAG) == 0:
            for (key, value) in attrs:
                if cmp(key, self.HREF_ATTRIBUTE) == 0:
>>>>>>> 11f1c3bede76edb13378e2376de5691b5709e411
                    self.links.append(value)

    def handle_endtag(self, tag):
        pass


class CrawlerThread(threading.Thread):
<<<<<<< HEAD
    def __init__(self, binarySemaphore, url, crawlDepth):
        self.binarySemaphore = binarySemaphore
        self.url = url
        self.crawlDepth = crawlDepth
=======
    def __init__(self, binarySemaphore, url):
        self.binarySemaphore = binarySemaphore
        self.url = url
>>>>>>> 11f1c3bede76edb13378e2376de5691b5709e411
        self.threadId = hash(self)
        threading.Thread.__init__(self)

    def run(self):
<<<<<<< HEAD
        socket = urllib.urlopen(self.url)
        urlMarkUp = socket.read()
        print(self.getName())
        linkHTMLParser = LinkHTMLParser()
        linkHTMLParser.feed(urlMarkUp)
        #self.binarySemaphore.acquire()  # wait if another thread has acquired and not yet released binary semaphore
        urls = []
        #for link in linkHTMLParser.links:
         #   link = urlparse.urljoin(self.url, link)
         #   urls.append(link)
         #   print("\t" + link)
        #self.binarySemaphore.release()
        #for url in urls:
            # Keep crawling to different urls until the crawl depth is less than 1
         #   if self.crawlDepth > 1:
         #       CrawlerThread(binarySemaphore, url, self.crawlDepth - 1).start()


if __name__ == "__main__":
    binarySemaphore = threading.Semaphore(1)
    urls = [("http://www.cnn.com", 2),("http://www.google.com", 1), ("http://www.facebook.com", 1)]
    #for (url, crawlDepth) in urls:
    CrawlerThread(binarySemaphore, "http://www.cnn.com" , 1).start()
    CrawlerThread(binarySemaphore, "http://www.google.com", 1).start()
    CrawlerThread(binarySemaphore, "http://www.facebook.com", 1).start()
    CrawlerThread(binarySemaphore, "http://www.youtube.com", 1).start()
    CrawlerThread(binarySemaphore, "http://www.andesonline.com", 1).start()
    CrawlerThread(binarySemaphore, "http://www.losandes.com.ar", 1).start()
    CrawlerThread(binarySemaphore, "http://fiat.com.ar", 1).start()
=======

        socket = urllib.urlopen(self.url)
        urlMarkUp = socket.read()
        linkHTMLParser = LinkHTMLParser()
        linkHTMLParser.feed(urlMarkUp)
        #self.binarySemaphore.acquire()  # wait if another thread has acquired and not yet released binary semaphore
        print (self.getName())
        urlsin=self.url.split('/')
        archivo = open(urlsin[2]+".txt" , 'a' )
        urls = []
        for link in linkHTMLParser.links:
            link = urlparse.urljoin(self.url, link)
            urls.append(link)
            print "\t" + link
            archivo.write(link +"\n")
        print ""
        #self.binarySemaphore.release()

>>>>>>> 11f1c3bede76edb13378e2376de5691b5709e411
