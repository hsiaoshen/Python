#coding=utf-8
#Gevent

import gevent
import urllib2
# from gevent import monkey;monkey.patch_all()

def foo(a):
    print "Running in foo",a
    urllib2.urlopen('http://www.newbieol.com')
    # gevent.sleep(4)   # 不像time中的sleep是进程休眠,这的是IO阻塞
    print 'switch to foo again'

def bar():
    print "Running in bar"
    gevent.sleep(3)
    print 'switch to bar again'

f = gevent.spawn(foo,1)
b = gevent.spawn(bar)

gevent.joinall([f,b])