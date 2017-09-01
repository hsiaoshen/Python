#coding=utf-8

# 手动写一个http服务器

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # self.rfile.read()
        print self.rfile.read(128)
        self.wfile.write('hello world')
        return

    def do_POST(self):
        
        return

address = ('127.0.0.1',3000)
server = HTTPServer(address,RequestHandler)
server.serve_forever()