from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import httplib
from urlparse import urlparse
import os,sys
import socket

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr

    def handle_endtag(self, tag):
        print "End tag  :", tag

    def handle_data(self, data):
        print "Data     :", data

    def handle_comment(self, data):
        print "Comment  :", data

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c

    def handle_decl(self, data):
        print "Decl     :", data

class html(object):
 
	def __init__(self):
		pass
 
	"""
	Funcion que realiza la conexion.
	Tiene que recibir: la url
	"""
	def html_connect(self,url):
		socket.setdefaulttimeout(20)
		try:
			parse=urlparse(url)
			if parse.scheme=="http":
				#self.conn=httplib.HTTPConnection(parse.netloc,timeout=60)
				self.conn=httplib.HTTPConnection(parse.netloc)
			else:
				#self.conn=httplib.HTTPSConnection(parse.netloc,timeout=60)
				self.conn=httplib.HTTPSConnection(parse.netloc)
			if parse.path=="":
				# Si no disponemos de path le ponemos la barra
				path="/"
			elif parse.query:
				# Si disponemos de path y query, realizamos el montaje
				path="%s?%s" % (parse.path,parse.query)
			else:
				# Si solo disponemos de path
				path=parse.path
			self.conn.request("GET",path)
			self.response1=self.conn.getresponse()
			self.status=self.response1.status
			self.reason=self.response1.reason
			self.headers=self.response1.getheaders()
		except socket.error:
			#errno, errstr = sys.exc_info()[:2]
			#if errno == socket.timeout:
				#print "There was a timeout"
			#else:
				#print "There was some other socket error"
			self.status=408
		except:
			self.status=404
 
	"""Muestra el estado"""
	def html_showStatus(self):
		try:
			return self.status, self.reason
		except:
			return ""
 
	"""Lee el contenido"""
	def html_read(self):
		self.read1=self.response1.read()
 
	"""Muestra el contenido"""
	def html_showHTML(self):
		if self.read1:
			return self.read1
		return ""
 
	"""Cierra la conexion"""
	def html_close(self):
		try:
			self.conn.close()
		except:
			pass

if __name__=="__main__":
        obj=html()
        obj.html_connect("http://www.um.edu.ar/es/")
        obj.html_read()
        buff = obj.html_showHTML()
	
        parser = MyHTMLParser()
        parser.feed(buff)
        obj.html_close()
