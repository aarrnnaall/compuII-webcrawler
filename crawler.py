import threading, urllib
from urllib.parse import urlparse
from urllib.parse import urljoin
from html.parser import HTMLParser
import urllib.request
import sys
from glob import glob
import fileinput
import time
from concurrent import futures
import os, signal
#lock = threading.Lock()
def run(url):
    print(format(threading.current_thread().name))
    #lock.acquire()
    try:
        socket = urllib.request.urlopen(url)
    except:
        print("Error Temporary failure in name resolution")
        socket = urllib.request.urlopen(url)
    urlMarkUp = socket.read().decode("ascii", "ignore")
    print("Llega URL al crawler: %s" % url)
    global linkHTMLParser
    linkHTMLParser = LinkHTMLParser()
    linkHTMLParser.feed(urlMarkUp)
    urlsin = url.split('/')
    archivomod = open(urlsin[2] + ".txt", 'a')
    archivoleer = open(urlsin[2] + ".txt", 'r')
    contenido = archivoleer.read()
    urls = []
    if contenido == '':
        for link in linkHTMLParser.links:
            link = urljoin(url, link)
            urls.append(link)
            print("\t" + link)
            #cola.put(link)
            archivomod.write(link + "\n")
        #cola.put("False")
        archivomod.close()
    else:
    #    input = fileinput.input(glob(urlsin[2] + ".txt"))
    #    for linea in input:
    #        cola.put(linea)
    #    cola.put("False")
    #    input.close()
        print("<Ya cargado Url %s >"%url)
        #os.kill(os.getpid(), signal.SIGKILL)
    #    lock.release()
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


def crawler(url):
        print("Empezando Crawler-URL")
        print("<Executing on %d >" % os.getpid())
        for elem in url:
            print("<Con URL: %s >" %elem)
            print("{}".format(futures.ThreadPoolExecutor(max_workers=5).submit(run, elem)))
            time.sleep(5)
