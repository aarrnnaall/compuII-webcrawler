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
        """Add all 'href' links within 'a' tags to self.links"""
        if cmp(tag, self.A_TAG) == 0:
            for (key, value) in attrs:
                if cmp(key, self.HREF_ATTRIBUTE) == 0:
                    self.links.append(value)

    def handle_endtag(self, tag):
        pass


class CrawlerThread(threading.Thread):
    def __init__(self, binarySemaphore, url):
        self.binarySemaphore = binarySemaphore
        self.url = url
        self.threadId = hash(self)
        threading.Thread.__init__(self)

    def run(self):

        socket = urllib.urlopen(self.url)
        urlMarkUp = socket.read()
        linkHTMLParser = LinkHTMLParser()
        linkHTMLParser.feed(urlMarkUp)
        self.binarySemaphore.acquire()  # wait if another thread has acquired and not yet released binary semaphore
        print (self.getName())
        urls = []
        for link in linkHTMLParser.links:
            link = urlparse.urljoin(self.url, link)
            urls.append(link)
            print "\t" + link
        print ""
        self.binarySemaphore.release()

