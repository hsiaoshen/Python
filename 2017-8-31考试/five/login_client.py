#coding=utf-8

# 注册登录的客户端

from socket import *
import sys
import getpass

HOST = sys.argv[1]
PORT = int(sys.argv[2])
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket()
sockfd.connect(ADDR)

def command():
    print '''
    1. login
    2. register
    '''

while True:
    command()
    try:
        cmd = raw_input('命令 ->>>')
        if (cmd != '1') and (cmd != '2'):
            break
        name = raw_input('name ->>>')
        passwd = getpass.getpass('passwd ->>>')
        if not (name and passwd):
            print '账号和密码不能为空'             
        sockfd.send('{},{},{}'.format(cmd,name,passwd))
    except Exception as e:
        print e
    data,time = sockfd.recv(BUFSIZE)
    print time
    d = {'200':'register OK!','201':'login OK!','400':'user already exsits','401':'passwd error','402':'user no exsits'}
    print d[data]
    if not data:
        break

sockfd.close()
