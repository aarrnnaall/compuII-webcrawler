from BaseHTTPServer import BaseHTTPRequestHandler
from os import curdir, sep
from crawler import Crawler
from imagen import Imagen
import cgi
from consulta import Consulta
from threading import Lock, Thread
from multiprocessing import Process, Queue
import sys
import threading
import fileinput
import os
cond=threading.Condition()
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        # if self.path=="/":

        try:
            # Check the file extension required and
            # set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True

            if sendReply == True:
                # Open the static file requested and send it
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
    # Handler for the POST requests

    def do_POST(self):
        if self.path == "/sendurl":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            ing_url = form["url"].value
            urls = ing_url.split()
            q = Queue()
            for url in urls:
                u = threading.Thread(target=Crawler(url,q,cond).crawler())
                u.start()
                print(u)
                print("con ID of process running: {}".format(os.getpid()))

            i = Process(target=Imagen(q.get(), url).imagen())
            i.start()
            print(i)
            print("con ID of process running: " + str(i.pid))
            print ("URl: %s" % ing_url)
            self.send_response(200)
            self.end_headers()
            archivoleer = open("resultado.html", 'r')
            html = archivoleer.read()
            self.wfile.write("%s " % html)
            for url in urls:
                self.wfile.write("<h1> %s " %url+"<h1>")
                self.wfile.write("<br>")
            return

        if self.path == "/sendconsulta":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            nom_const = form["consulta"].value
            urls_buscar = []
            c = threading.Thread(target=Consulta(nom_const,urls_buscar,cond).consulta())
            c.start()
            print(c)
            print("con ID of process running: {}".format(os.getpid()))
            print ("Buscado: %s" % nom_const)
            self.send_response(200)
            self.end_headers()
            archivoleer = open("resultado.html", 'r')
            html = archivoleer.read()
            self.wfile.write("%s " % html)
            if(urls_buscar):
                for linea in urls_buscar:
                    self.wfile.write("<a href= %s"% linea+">%s"% linea+"</a>" )
                    self.wfile.write("<br><br>")
            else:
                self.wfile.write("<h2>No hay resultados<h2>")


            return
