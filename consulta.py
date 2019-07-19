import mmap

class consultahtml(object):

    def __init__(self,palabra):
        buff_buscar = [] 
        palabra_esp= palabra.split(" ")
        files = open('cont.txt', 'r') 
        mapear = mmap.mmap(files.fileno(), 0, access=mmap.ACCESS_READ) 
        #for palabra_bus in palabra_esp: 
        for palabra_bus in palabra_esp:
            while(True):
                a=palabra_bus
                linea = mapear.readline()
                if a in linea:
                    print("---------------------------------------------------------------"+a)
                    buff_buscar.append(linea)
                    a=None
                else:
                    if a.title() in linea:
                        buff_buscar.append(linea)
                        a=None
                if not linea:
                    break
         
        if buff_buscar == []:
            print("No se encontro Nada")
        else:
            buff = "".join(buff_buscar)
            print(buff) 
    

            
