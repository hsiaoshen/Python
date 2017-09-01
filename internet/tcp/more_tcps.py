#coding=utf-8

from socket import *
from time import ctime
from multiprocessing import Pool

HOST = '127.0.0.1'
PORT = 3000
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.bind(ADDR)
sockfd.listen(10)

def speek(addr):
    print addr
    while True:
        data = connfd.recv(BUFSIZE)
        if  data == "\r\n":
            break
        print data
        connfd.sendall('[%s]\n'%ctime())
    connfd.close()
    sockfd.close()

t = []

pool = Pool(10)

if __name__ == '__main__':
    while True:
        print('waiting for connection...')
        connfd,addr = sockfd.accept()
        print("connected from :",addr)
        if addr is exit:
            t[addr] = pool.apply_async(func=speek,args=(addr,))
            
        
  








