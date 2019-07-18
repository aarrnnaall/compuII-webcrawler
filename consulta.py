import mmap

class consultahtml(object):

    def __init__(self,palabra):
        buff_buscar = [] 
        files = open('cont.txt', 'r') 
        mapear = mmap.mmap(files.fileno(), 0, access=mmap.ACCESS_READ) 
        while(True):
            linea = mapear.readline()
            if palabra in linea:
                buff_buscar.append(linea)
            if not linea:
                break
        buff = "".join(buff_buscar)
        print(buff) 
    

            
