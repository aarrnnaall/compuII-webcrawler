import mmap
import threading
from os import listdir
from glob import glob
import fileinput
import sys
import time
import os, signal
from concurrent import futures

def buscarUrl(palabra):
    print(format(threading.current_thread().name))
    link = glob('*.txt')
    if(link):
        input = fileinput.input(link)
        for linea in input:
            if palabra in linea:
                print(linea)
            if not linea:
                break
        input.close()
    else:
        print("No esta Cargado Nada")

def buscarImg(palabra):
    print(format(threading.current_thread().name))
    img = glob('*/*')
    if(img):
        for elem in img:
            try:
                ext=(elem.split("/")[1]).split(".")[1]
                if(ext=="png" or ext=="jpg" or ext=="gif" or ext=="jpeg" or ext=="eps"):
                    if palabra in elem.split("/")[1]:
                        print(elem.split("/")[1])
                    if not linea:
                        break
            except:
                pass
    else:
        print("No esta Cargado Nada")

def consulta(palabra):
            print("Empezando Consulta-URL-Imagen")
            print("<Executing on %d >" % os.getpid())
            with futures.ThreadPoolExecutor(max_workers=2) as executor:
                for elem in palabra:
                    print("<Buscando: %s >" % elem)
                    future_to_url = executor.submit(buscarUrl,elem)
                    print("Url: %s" % future_to_url)
                    future_to_url2 = executor.submit(buscarImg, elem)
                    print("Imagen: %s" % future_to_url2)


