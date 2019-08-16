from BaseHTTPServer import BaseHTTPRequestHandler
from os import curdir, sep
from webcrawler import CrawlerThread
import cgi
import re
from hiloconsulta import MiHilocons
import threading
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
	    #if self.path=="/":
		    
		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

	#Handler for the POST requests
	def do_POST(self):
                if self.path=="/sendurl":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
                        ing_url = form["url"].value
                        urls=ing_url.split()
                        #urls=[("https://www.chevrolet.com.ar/")]
                        binarySemaphore = threading.Semaphore(1)
                        for url in urls:
                            CrawlerThread(binarySemaphore, url).start()
<<<<<<< HEAD
             #               CrawlerThread(url).start()
                        print(urls)
=======
                       #print(urls)
>>>>>>> 9f460ee3c4334d917ef73e2e1a5db6b7e691e6a6
                        
                        print "URl: %s" % ing_url
			self.send_response(200)
			self.end_headers()
                        self.wfile.write("Thanks for this URL: %s " % ing_url)
			return 		
			
                if self.path=="/sendconsulta":
                        form = cgi.FieldStorage(
                                fp=self.rfile,
                                headers=self.headers,
                                environ={'REQUEST_METHOD':'POST',
                                 'CONTENT_TYPE':self.headers['Content-Type'],
                        })
                        nom_const = form["consulta"].value
                        hMiHilo = MiHilocons(nom_const)
                        hMiHilo.start()

                        print "Buscado: %s" % nom_const
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write("Thanks for this Search: %s " % nom_const)
                        return


