import threading

class MiHilo(threading.Thread):
    def __init__(self, pParam1, pParam2, pParam3):
	threading.Thread.__init__(self)
	self.pParam1 = pParam1
	self.pParam2 = pParam2
        self.pParam3 = pParam3
	self.stoprequest = threading.Event()
        print(self.getName())
