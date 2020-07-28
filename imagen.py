import requests
import threading
from bs4 import BeautifulSoup
import multiprocessing
from bs4 import BeautifulSoup as BSHTML
import urllib3
import os
from glob import glob
import time
class Thread(threading.Thread):
    def __init__(self,url):
        self.url = url
        self.threadId = self
        threading.Thread.__init__(self)

    def run(self):
        print(self.getName())
        try:
            print("Url: %s" % self.url)
            http = urllib3.PoolManager()
            try:
                response = http.request('GET', self.url)
                soup = BSHTML(response.data, "html.parser")
                global images
                images = soup.findAll('img')
            except:
                print("Error No host specified.")
            links = []
            dire = self.url.split("//")[1]
            dir = dire.split("/")[0]
            print("Dir: %s" % dir)
            try:
                os.stat(dir.split("/")[0])
            except:
                os.mkdir(dir.split("/")[0])
            try:
                global images
                for image in images:
                    links.append(image['src'])
            except KeyError:
                    print("Error src")
            for elem in links:
                link = glob(dir.split("/")[0] + "/" + elem.split("/")[len(elem.split("/")) - 1])
                if link:
                    print("Imagen Existente")
                else:
                    try:
                        elem.split("http://")[1]
                        url_imagen = elem  # El link de la imagen
                        #print("CON http://")
                        print("URL Imagen: %s " % url_imagen);
                        nombre_local_imagen = dir.split("/")[0] + "/" + elem.split("/")[
                            len(elem.split("/")) - 1]  # El nombre con el que queremos guardarla
                        imagen = requests.get(url_imagen).content
                        with open(nombre_local_imagen, 'wb') as handler:
                            handler.write(imagen)

                    except(IndexError):
                        http = self.url.split("/")[0] + "//" + self.url.split("/")[2] + "/"
                        url_imagen = http + elem  # El link de la imagen
                        #print("SIN http://")
                        print("URL Imagen: %s " % url_imagen);
                        nombre_local_imagen = dir.split("/")[0] + "/" + elem.split("/")[
                            len(elem.split("/")) - 1]  # El nombre con el que queremos guardarla
                        imagen = requests.get(url_imagen).content
                        with open(nombre_local_imagen, 'wb') as handler:
                            handler.write(imagen)
        except requests.ConnectionError:  # This is the correct syntax
                print("Error Temporary failure")

class Imagen():

    def __init__(self, cola):
        self.cola=cola

    def imagen(self):

            print("Empezando Imagen")
            if(self.cola.empty()):
                print("Cola Vacia")
            else:
                #print("Cola Llena")
                start_time = time.time()
                while not self.cola.empty():
                    url = self.cola.get()
                    Thread(url).start()
                end_time = time.time()
                print("Tiempo Crawler-Imagen: %s" % str(end_time - start_time))
                print("Imagen Realizada")


