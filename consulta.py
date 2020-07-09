import mmap
import threading
from os import listdir
from glob import glob
import fileinput
import sys
import time

class MiHilocons(threading.Thread):

    def __init__(self, palabra,cond):
        threading.Thread.__init__(self)
        self.cond= cond
        self.palabra = palabra
        print(self.getName())

    def consult(self):
        link = glob('*.txt')
        for linea in fileinput.input(link):
            if self.palabra in linea:
                print(linea)
            if not linea:
                break

    def run(self):
        self.consult()
        #self.cond.acquire()
        #self.cond.wait()
        #self.cond.release()

