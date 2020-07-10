import requests
from bs4 import BeautifulSoup
import multiprocessing
from bs4 import BeautifulSoup as BSHTML
import urllib3

class Imagen():

    def __init__(self, url):
        self.url=url

    def imagen(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.url)
        soup = BSHTML(response.data, "html.parser")
        images = soup.findAll('img')
        links = []
        for image in images:
            links.append(image['src'])
            print(links[0])
        print("Realizado Imagen!")