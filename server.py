import http.server
import socketserver

port=8000

handler= http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",port),handler) as httpd:
    print("serving at port",port)
    http.server_forever()
