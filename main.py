from server import myHandler
from http.server import HTTPServer
from server import HTTPServerV6
from threading import Thread
PORT_NUMBER = 8080

try:
        server_ipv4 = HTTPServer(('', PORT_NUMBER), myHandler)
#        server_ipv6 = HTTPServerV6(('::1', PORT_NUMBER), myHandler)
        print ('Started httpserver on port ' , PORT_NUMBER)
        print('Starting server, use <Ctrl-C> to stop')
        th4 = Thread(target=server_ipv4.serve_forever)
#        th6 = Thread(target=server_ipv6.serve_forever)
        th4.start()
#        th6.start()
        print("Hilo IPV4 --> %s" % th4)
#        print("Hilo IPV6 --> %s" % th6)

except KeyboardInterrupt:
        server.socket.close()

