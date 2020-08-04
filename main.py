from server import myHandler
from http.server import HTTPServer
from threading import Thread
import multiprocessing
import socket
from server import ThreadedHTTPServer
from server import ThreadedHTTPServerV6
from socketserver import ThreadingMixIn
import argparse
from configparser import ConfigParser
parser = ConfigParser()
parser.read('config_init.ini',encoding='utf-8')
port = parser.get('config_init', 'port')

if int(port):
        PORT_NUMBER=int(port)
        try:
                        server_ipv4 = ThreadedHTTPServer(('', PORT_NUMBER), myHandler)
                        server_ipv6 = ThreadedHTTPServerV6(('::1', PORT_NUMBER), myHandler)
                        print('Started httpserver on port ', PORT_NUMBER)
                        print('Starting server, use <Ctrl-C> to stop')
                        th4 = multiprocessing.Process(target=server_ipv4.serve_forever, name="IPV4")
                        th6 = multiprocessing.Process(target=server_ipv6.serve_forever, name="IPV6")
                        th4.start()
                        th6.start()
                        print("Process IPV4 --> %s" % th4)
                        print("Process IPV6 --> %s" % th6)
                        th4.join()
                        th6.join()

        except KeyboardInterrupt:
                        pass
                        th4.terminate()
                        th6.terminate()
                        server_ipv4.socket.close()
                        server_ipv6.socket.close()
                        print("\nTermino Servidor")


