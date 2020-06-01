import mmap
import threading
from os import listdir
from glob import glob
import fileinput
import sys

class MiHilocons(threading.Thread):

    def __init__(self, palabra):
        threading.Thread.__init__(self)
        self.palabra = palabra
        print(self.getName())

    def run(self):
        link = glob('*.txt')
        for linea in fileinput.input(link):
            if self.palabra in linea:
                print(linea)
            
