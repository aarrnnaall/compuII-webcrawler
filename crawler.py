import threading, urllib, urlparse
from HTMLParser import HTMLParser
import sys
import fileinput

class LinkHTMLParser(HTMLParser):
    A_TAG = "a"
    HREF_ATTRIBUTE = "href"

    def __init__(self):
        self.links = []
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if cmp(tag, self.A_TAG) == 0:
            for (key, value) in attrs:
                if cmp(key, self.HREF_ATTRIBUTE) == 0:
                    self.links.append(value)

    def handle_endtag(self, tag):
        pass


class Crawler():
    def __init__(self, url,cond):
        self.url = url
        self.cond=cond

    def crawler(self):
        socket = urllib.urlopen(self.url)
        urlMarkUp = socket.read()
        linkHTMLParser = LinkHTMLParser()
        linkHTMLParser.feed(urlMarkUp)
        urlsin=self.url.split('/')
        archivomod = open(urlsin[2]+".txt" , 'a' )
        archivoleer = open(urlsin[2] + ".txt", 'r')
        contenido = archivoleer.read()
        urls = []
        self.cond.acquire()
        for link in linkHTMLParser.links:
            link = urlparse.urljoin(self.url, link)
            urls.append(link)
            if contenido == '':
                print("\t" + link)
                archivomod.write(link + "\n")
        if contenido != '':
            print("Ya cargado!")
        self.cond.notify()
        self.cond.release()
