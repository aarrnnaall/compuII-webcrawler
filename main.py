from server import myHandler
from BaseHTTPServer import HTTPServer

PORT_NUMBER = 8081

try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        #server.do_GET("index.html")
        #server.do_POST("/send")
        print ('Started httpserver on port ' , PORT_NUMBER)

        #Wait forever for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        server.socket.close()

