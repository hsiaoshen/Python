#coding=utf-8

# 手动写一个http服务器实现文件的下载和上传，查看

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # self.rfile.read()
        print self.rfile.read(128)
        self.wfile.write('hello world')
        return


    def do_POST(self):   
        return

# address = ('127.0.0.1',3000)
# server = HTTPServer(address,RequestHandler)

while True:
        print ('''         Command        ''')
        print ('<<<1. download......>>>')
        print ('<<<2. put...........>>>')
        print ('<<<3. ls............>>>')
        print ('<<<4. exit..........>>>')
        filename = raw_input('请输入编号>>')

        if(filename =='4'):
            break

# if __name__ == '__main__':


#     server.serve_forever()