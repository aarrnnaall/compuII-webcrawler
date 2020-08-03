from server import myHandler
from http.server import HTTPServer
from server import HTTPServerV6
from threading import Thread
import multiprocessing
import socket
from socketserver import ThreadingMixIn
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="Puerto del Servidor", type=int, default=8080)
#parser.add_argument("-u", "--url", help="Cantidad de Hilos en Crawler-Url", type=int, default=0)
#parser.add_argument("-i", "--imagen", help="Cantidad de Hilos en Crawler-Imagenes",type=int, default=0)
#parser.add_argument("-c", "--profun", help="Profundidad de Crawler-Imagen", type=int, default=1)
args = parser.parse_args()

def arg_url():
     return args.url
def arg_img():
     return args.imagen+"/"+args.profun

if args.port or args.imagen or args.url or args.profun:
        PORT_NUMBER=args.port
        try:
                server_ipv4 = HTTPServer(('', PORT_NUMBER), myHandler)
                server_ipv6 = HTTPServerV6(('::1', PORT_NUMBER), myHandler)
                print ('Started httpserver on port ' , PORT_NUMBER)
                print('Starting server, use <Ctrl-C> to stop')
                try:
                        th4 = multiprocessing.Process(target=server_ipv4.serve_forever)
                        th6 = multiprocessing.Process(target=server_ipv6.serve_forever)
                        th4.start()
                        th6.start()
                        print("Process IPV4 --> %s" % th4)
                        print("Process IPV6 --> %s" % th6)
                        th4.join()
                        th6.join()
                except KeyboardInterrupt:
                        th4.terminate()
                        th6.terminate()
                        print("\nProcesos Terminado")
        except Exception:
                server_ipv4.socket.close()
                server_ipv6.socket.close()


