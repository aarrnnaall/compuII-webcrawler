import threading
import time 

class MiHilo(threading.Thread):
 
    def __init__(self,in_queue,cond):
        threading.Thread.__init__(self)
        self.in_queue = in_queue
        self.cond = cond
        

    def run(self):
        archivo=open('cont.txt','a')
        print(self.getName())
        while True:
            self.cond.acquire()
            #cond.wait()
            if not self.in_queue.empty():
                sac = self.in_queue.get()
                print("Sacando----> "+ sac)   
                #archivo.write(sac+"\n")
            self.cond.notify()
            self.cond.release()
