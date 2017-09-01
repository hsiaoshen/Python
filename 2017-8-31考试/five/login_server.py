#coding=utf-8

# 注册登录的服务器，把信息存储在mysql数据库中

from socket import *
import gevent
from gevent import monkey;monkey.patch_all()
from time import ctime
import MySQLdb
import getpass 

user = raw_input('用户名：')
password = getpass.getpass('密码：')

db = MySQLdb.connect('localhost',user,password,'testdb')
print 'db connected OK!'

def server(port):
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
    s.bind(('0.0.0.0',port))
    s.listen(10)
    while True:
        cli,addr = s.accept()
        gevent.spawn(handler,cli)

def login(db,name,password):
    cursor = db.cursor()
    result = cursor.execute('select * from login where name="%s"'%(name))
    if result:
        pd = cursor.execute('select passwd from login where name="%s"'%(name))
        if pd == password:
            return '201'
        else:
            return '401'
    else:
        return '402'


def register(db,name,passwd):
    cursor = db.cursor()
    result = cursor.execute('select * from login where name="%s"'%(name))
    if result:
        return '400'
        cursor.close()
    else:
        try:
            # print name,passwd,flog
            cursor.execute("insert into login (name,passwd) values ('%s','%s')"%(name,passwd))
            db.commit()
            return '200'
            cursor.close()
        except:
            db.rollback()
            cursor.close()

def handler(conn):
    try:
        data = conn.recv(1024)
        l = data.split(',')
        print l
        cmd = l[0]
        name = l[1]
        passwd = l[2]
        if cmd == '1':
            data = login(db,name,passwd)
        elif cmd == '2':
            data = register(db,name,passwd)             
        conn.send(data) 
    except Exception as e:
        print e
    finally:
        conn.close()

if __name__ == "__main__":
    server(3000)                