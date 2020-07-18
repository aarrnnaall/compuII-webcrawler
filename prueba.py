
from img import Img
import threading
from multiprocessing import Process, Queue

def prueba():

    url = 'http://www.umaza.edu.ar/'

    p = Process(target=Img(url).img())
    p.start()
    p.join

prueba()