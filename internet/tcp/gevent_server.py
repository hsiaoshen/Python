#coding=utf-8

# 协程实现高并发服务器

import gevent
from gevent import monkey;monkey.patch_all()
from time import ctime
from socket import *

def server(port):
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
    s.bind(('0.0.0.0',port))
    s.listen(10)
    while True:
        cli,addr = s.accept()
        gevent.spawn(handler,cli)

def handler(conn):
    try:
        while True:
            data = conn.recv(1024)
            print 'recv:',data
            conn.send(ctime())
            if not data:
                break
    except Exception as e:
        print e

    finally:
        conn.close()

if __name__ == "__main__":
    server(3000)                