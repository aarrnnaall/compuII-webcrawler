import threading, urllib2, urlparse
from HTMLParser import HTMLParser
import sys
from bs4 import BeautifulSoup
import requests

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
	  threading.Thread.__init__(self)

      def run(self):
      	  """Print out all of the links on the given url associated with this particular thread. Grab the passed in 
	  binary semaphore when attempting to write to STDOUT so that there is no overlap between threads' output."""
	  #socket = requests.get(self.url)
          #urlMarkUp = socket.text
          socket = urllib2.urlopen(self.url)  
	  urlMarkUp = socket.read()
	  linkHTMLParser = LinkHTMLParser()
	  linkHTMLParser.feed(urlMarkUp)
      	  self.binarySemaphore.acquire() # wait if another thread has acquired and not yet released binary semaphore
	  print (self.getName())
          print "Url %s" %(self.url)
      	  #print "Retreived the following links..." %(self.threadId)
	  urls = []
	  archivo=open('cont.txt','a')
          for link in linkHTMLParser.links:
	      link = urlparse.urljoin(self.url, link)
	      urls.append(link)
      	  
          url_sinrep=[]
          for elemento in urls:
              if not elemento in url_sinrep:
                  url_sinrep.append(elemento)
          for url_most in url_sinrep:
              print "\t"+url_most
              req = requests.get(url_most)
              soup = BeautifulSoup(req.text, "lxml")
              try: 
                 title = soup.title.string.encode('utf-8')  
              except Exception:
                 title=" "
                 pass
              if title == "400":
                 title = ""
              archivo.write(url_most+" ")
              archivo.write(title+"\n")
              print("\t\t"+title)

          self.binarySemaphore.release()	     	 