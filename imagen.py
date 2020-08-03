import requests
import threading
from bs4 import BeautifulSoup
import multiprocessing
from bs4 import BeautifulSoup as BSHTML
import urllib3
import os
from glob import glob
import time
#import numpy as np
from concurrent import futures
import os

def run(url):
    print(format(threading.current_thread().name))
    print("<Executing on %d >"%os.getpid())
    img = []
    try:
        print("Url: %s" % url)
        http = urllib3.PoolManager()
        try:
            response = http.request('GET', url)
            soup = BSHTML(response.data, "html.parser")
            global images
            images = soup.findAll('img')
        except:
            images = soup.findAll('img')
            print("Error No host specified.")
        links = []
        dire = url.split("//")[1]
        dir = dire.split("/")[0]
        print("Dir: %s" % dir)
        try:
            os.stat(dir.split("/")[0])
        except:
            os.mkdir(dir.split("/")[0])
        try:
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
                    img.append(url_imagen)
                    nombre_local_imagen = dir.split("/")[0] + "/" + elem.split("/")[
                        len(elem.split("/")) - 1]  # El nombre con el que queremos guardarla
                    imagen = requests.get(url_imagen).content
                    with open(nombre_local_imagen, 'wb') as handler:
                        handler.write(imagen)

                except(IndexError):
                    http = url.split("/")[0] + "//" + url.split("/")[2] + "/"
                    url_imagen = http + elem  # El link de la imagen
                    img.append(url_imagen)
                    #print("SIN http://")
                    print("URL Imagen: %s " % url_imagen);
                    nombre_local_imagen = dir.split("/")[0] + "/" + elem.split("/")[
                        len(elem.split("/")) - 1]  # El nombre con el que queremos guardarla
                    imagen = requests.get(url_imagen).content
                    with open(nombre_local_imagen, 'wb') as handler:
                        handler.write(imagen)
    except requests.ConnectionError:  # This is the correct syntax
            print("Error Temporary failure")
    return img


def imagen(cola,p,cola2):
           print("Empezando Crawler-Imagen")
           print("<Executing on %d >" % os.getpid())
           with futures.ThreadPoolExecutor(max_workers=2) as executor:
                #while True:
                for i in range(p):
                    url = cola.get()
                    if (url == "False"):
                        print("Termino")
                        break
                    future_to_url = executor.submit(run, url)
                print(future_to_url)
                prof=i+1
                print("Profundidad Imagen %d" %prof)
           for elem in future_to_url.result():
               cola2.put(elem)
           print("Imagen Realizada")


