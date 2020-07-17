import requests
from bs4 import BeautifulSoup
import multiprocessing
from bs4 import BeautifulSoup as BSHTML
import urllib3
import os
class Imagen():

    def __init__(self, url,direc):
        self.url=url
        self.direc=direc

    def imagen(self):
        print("Cargando Imagenes....")
        http = urllib3.PoolManager()
        response = http.request('GET', self.url)
        soup = BSHTML(response.data, "html.parser")
        images = soup.findAll('img')
        links = []
        dir=self.direc.split("//")[1]
        try:
            os.stat(dir.split("/")[0])
        except:
            os.mkdir(dir.split("/")[0])
        for image in images:
            links.append(image['src'])
        for elem in links:
            try:
                url_imagen = elem  # El link de la imagen
                nombre_local_imagen = dir.split("/")[0]+"/"+elem.split("/")[len(elem.split("/"))-1]  # El nombre con el que queremos guardarla
                imagen = requests.get(url_imagen).content
                with open(nombre_local_imagen, 'wb') as handler:
                    handler.write(imagen)
                break
            except:
                url_imagen = self.direc+elem  # El link de la imagen
                nombre_local_imagen = dir.split("/")[0] + "/" + elem.split("/")[
                    len(elem.split("/")) - 1]  # El nombre con el que queremos guardarla
                imagen = requests.get(url_imagen).content
                with open(nombre_local_imagen, 'wb') as handler:
                    handler.write(imagen)
print("Realizado Imagen!")