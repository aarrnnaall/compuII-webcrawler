from crawler import CrawlerThread
from consulta import MiHilocons
from imagen import Imagen
import threading
from multiprocessing import Process, Queue

def prueba():

    url = 'https://www.google.com/?hl=es'
    q = Queue()
    q.put([10.5, False, "Recursos Python"])

    cond = threading.Condition()
    CrawlerThread(url,cond).start()
    MiHilocons("um",cond).start()

    p = Process(target=Imagen(url).imagen())
    p.start()
    p.join

prueba()