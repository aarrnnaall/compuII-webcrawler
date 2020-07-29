from http.server import HTTPServer,BaseHTTPRequestHandler
from os import curdir, sep
from crawler import crawler
import cgi
from consulta import consulta
import threading
import multiprocessing
from imagen import imagen
import os, signal
import time
from socketserver import ThreadingMixIn
from concurrent.futures import ProcessPoolExecutor
crawler_pipe, imagen_pipe = multiprocessing.Pipe()
class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:

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
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read().encode(encoding='utf_8'))
                f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

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
            q = multiprocessing.Queue()
            executor = ProcessPoolExecutor(max_workers=2)
            print("Proceso Crawler-Url: {}".format(executor.submit(crawler,urls)))
                #time.sleep(10)
           # IMG = executor.submit(imagen,q)
           # print("Proceso Crawler-Imagen: {}".format(IMG))

            print ("URl: %s" % ing_url)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(("Thanks for this URL: %s " % ing_url).encode(encoding='utf_8'))
            return

        if self.path == "/sendconsulta":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            nom_const = form["consulta"].value

            p = multiprocessing.Process(target=consulta(nom_const).start())
            p.start()
            print("Proceso Consulta-URL: %s " % p.name + "con ID: " + str(p.pid))
            print ("Buscado: %s" % nom_const)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(("Thanks for this Search: %s " % nom_const).encode(encoding='utf_8'))
            return
