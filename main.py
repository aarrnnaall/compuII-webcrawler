from server import myHandler
from http.server import HTTPServer

PORT_NUMBER = 8080

try:
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print ('Started httpserver on port ' , PORT_NUMBER)
        print('Starting server, use <Ctrl-C> to stop')
        server.serve_forever()

except KeyboardInterrupt:
        server.socket.close()

