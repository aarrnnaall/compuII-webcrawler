import mmap
import threading
from os import listdir
from glob import glob
import fileinput
import sys
import time
import threading
class consulta(threading.Thread):

    def __init__(self, palabra,cond):
        threading.Thread.__init__(self)
        self.cond= cond
        self.palabra = palabra
        print(self.getName())

    def consult(self):
        link = glob('*.txt')
        if(link):
             input = fileinput.input(link)
             for linea in input:
                if self.palabra in linea:
                    print(linea)
                if not linea:
                    break
             input.close()
        else:
             return False

    def run(self):
        cons = self.consult()
        if(cons==False):
            print("No se encontro")
        else:
            print("Ya cargado!")
