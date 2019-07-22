import mmap
import threading

class MiHilocons(threading.Thread):
 
    def __init__(self,palabra):
        threading.Thread.__init__(self)
        self.palabra = palabra
        print(self.getName())

    def run(self):
        buff_buscar = [] 
        palabra_esp= self.palabra.split(" ")
        files = open('cont.txt', 'r') 
        mapear = mmap.mmap(files.fileno(), 0, access=mmap.ACCESS_READ) 
        #for palabra_bus in palabra_esp:
        while(True):
            linea = mapear.readline()
            if self.palabra in linea:
                buff_buscar.append(linea)

            else:
                if self.palabra.title() in linea:
                    buff_buscar.append(linea)
        
            if not linea:
                break
         
        if buff_buscar == []:
            print("No se encontro Nada")
        else:
            buff = "".join(buff_buscar)
            print(buff) 
    

            
