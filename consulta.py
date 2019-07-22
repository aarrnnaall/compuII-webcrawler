import mmap

class consultahtml(object):

    def __init__(self,palabra):
        buff_buscar = [] 
        palabra_esp= palabra.split(" ")
        files = open('cont.txt', 'r') 
        mapear = mmap.mmap(files.fileno(), 0, access=mmap.ACCESS_READ) 
        #for palabra_bus in palabra_esp:
        while(True):
            linea = mapear.readline()
            if palabra in linea:
                buff_buscar.append(linea)

            else:
                if palabra.title() in linea:
                    buff_buscar.append(linea)
        
            if not linea:
                break
         
        if buff_buscar == []:
            print("No se encontro Nada")
        else:
            buff = "".join(buff_buscar)
            print(buff) 
    

            
