import mmap
import threading
from os import listdir
from glob import glob
import fileinput
import sys
import time

class Consulta(threading.Thread):

    def __init__(self, palabra,array):
        self.palabra = palabra
        self.array = array

    def buscar(self):
        link = glob('*/*.txt')
        if(link):
             input = fileinput.input(link)
             for linea in input:
                if self.palabra in linea:
                    self.array.append(linea)
                    print(linea)
                if not linea:
                    break
             input.close()
        else:
             return False

    def consulta(self):
        if(self.buscar()==False):
            print("No hay resultado")
            self.buscar()
        else:
            self.buscar()
