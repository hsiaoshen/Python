#coding=utf-8

#多路复用解决(select)高并发

from socket import *
from time import ctime
from select import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0',8888))
s.listen(10)


inputs = [s]

while True:
    rs,ws,es = select(inputs,[],[])
    for r in rs:
        if r is s:
            connfd,addr = r.accept()
            print 'connected form:',addr
            inputs.append(connfd)
        else:
            try:
                data = r.recv(1024)
                print 'recv:',data
                r.send(ctime())
                if not data:
                    inputs.remove(r)
                    r.close()
            except Exception as e:
                print e
s.close()