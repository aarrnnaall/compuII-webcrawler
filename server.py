from BaseHTTPServer import BaseHTTPRequestHandler
from os import curdir, sep
from crawler import Crawler
import cgi
from consulta import MiHilocons
import threading
import multiprocessing
from imagen import Imagen
import os
import time

crawler_pipe, imagen_pipe = multiprocessing.Pipe()
q = multiprocessing.Queue()
condition = multiprocessing.Condition()
lock = threading.Lock()
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
                self.wfile.write(f.read())
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
            lock.acquire()
            i = multiprocessing.Process(target=Crawler(urls,q).crawler())
            i.start()
            print("Proceso Crawler-URL: %s" % i + "con ID: " + str(i.pid))
            lock.release()
            #time.sleep(2)
            if (q.empty()):
                print("Cola Vacia")
            else:
                lock.acquire()
                i.join()
                u = multiprocessing.Process(target=Imagen(q).imagen())
                u.start()
                print("Proceso Crawler-Imagen: %s" % u + "con ID: " + str(u.pid))
                lock.release()
                u.join()
            print ("URl: %s" % ing_url)
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Thanks for this URL: %s " % ing_url)
            return

        if self.path == "/sendconsulta":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            nom_const = form["consulta"].value
            hMiHilo = MiHilocons(nom_const)
            hMiHilo.start()
            print("con ID of process running: {}".format(os.getpid()))
            print ("Buscado: %s" % nom_const)
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Thanks for this Search: %s " % nom_const)
            return
