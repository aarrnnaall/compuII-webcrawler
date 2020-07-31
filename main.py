from server import myHandler
from http.server import HTTPServer
from server import HTTPServerV6
from threading import Thread
import multiprocessing
import socket
from socketserver import ThreadingMixIn
PORT_NUMBER = 9090

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
                print("Process IPV4 --> %s" % th4)
                print("Process IPV6 --> %s" % th6)

        except KeyboardInterrupt:
                th4.terminate()
                th6.terminate()
                print("\nProcesos Terminado")
except Exception:
        server_ipv4.socket.close()
        server_ipv6.socket.close()


