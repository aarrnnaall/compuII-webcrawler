import threading
 
class MiHilo(threading.Thread):
 
    def __init__(self,url,title,desc):
        threading.Thread.__init__(self)
        self.url = url
        self.title = title
        self.desc = desc
        print(self.getName())

    def run(self):
        archivo=open('cont.txt','a')
        if self.title != "400":
            archivo.write(self.url+"  ")
            archivo.write(self.title+"  ")
        if self.desc != None:    
            archivo.write(self.desc+"  \n")

