import threading, urllib, urlparse
from HTMLParser import HTMLParser
import sys
import fileinput
import os
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
    def __init__(self, url,cola):
        self.url = url
        self.cola=cola

    def crawler(self):
        socket = urllib.urlopen(self.url)
        urlMarkUp = socket.read()
        linkHTMLParser = LinkHTMLParser()
        linkHTMLParser.feed(urlMarkUp)
        urlsin=self.url.split('/')
        dir = self.url.split("//")[1]
        try:
            os.stat(dir.split("/")[0])
        except:
            os.mkdir(dir.split("/")[0])

        archivomod = open(dir.split("/")[0]+"/"+"url."+urlsin[2]+".txt" , 'a' )
        archivoleer = open(dir.split("/")[0]+"/"+"url."+urlsin[2] + ".txt", 'r')
        contenido = archivoleer.read()
        urls = []
        for link in linkHTMLParser.links:
            link = urlparse.urljoin(self.url, link)
            urls.append(link)
            self.cola.put(link)
            if contenido == '':
                print("\t" + link)
                archivomod.write(link + "\n")
        if contenido != '':
            print("Ya cargado!")