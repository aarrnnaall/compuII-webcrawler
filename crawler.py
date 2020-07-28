import threading, urllib
from urllib.parse import urlparse
from urllib.parse import urljoin
from html.parser import HTMLParser
import urllib.request
import sys
from glob import glob
import fileinput
from imagen import Imagen
import time
class Thread(threading.Thread):
    def __init__(self, url, cola):
        self.url = url
        self.cola = cola
        self.threadId = self
        threading.Thread.__init__(self)

    def run(self):
        print(self.getName())
        try:
            socket = urllib.request.urlopen(self.url)
        except:
            print("Error Temporary failure in name resolution")
            socket = urllib.request.urlopen(self.url)
        urlMarkUp = socket.read().decode("ascii", "ignore")
        global linkHTMLParser
        linkHTMLParser = LinkHTMLParser()
        linkHTMLParser.feed(urlMarkUp)
        urlsin = self.url.split('/')
        archivomod = open(urlsin[2] + ".txt", 'a')
        archivoleer = open(urlsin[2] + ".txt", 'r')
        contenido = archivoleer.read()
        urls = []
        print("Empezando Crawler URL")
        if contenido == '':
            for link in linkHTMLParser.links:
                link = urljoin(self.url, link)
                urls.append(link)
                print("\t" + link)
                self.cola.put(link)
                archivomod.write(link + "\n")
            self.cola.put("False")
            archivomod.close()
        else:
            input = fileinput.input(glob(urlsin[2] + ".txt"))
            for linea in input:
                self.cola.put(linea)
            self.cola.put("False")
            input.close()
            print("Ya cargado!")

def cmp(a, b):
    return (a > b) - (a < b)


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

class Crawler(threading.Thread):
    def __init__(self, url,cola,cond):
        self.url = url
        self.cola = cola
        self.cond=cond

    def crawler(self):
        self.cond.acquire()
        #start_time = time.time()
        for url in self.url:
            Thread(url,self.cola).start()
        #end_time = time.time()
        self.cond.notify()
        self.cond.release()
        #print("Tiempo Crawler-Url: %s" % str(end_time-start_time))
