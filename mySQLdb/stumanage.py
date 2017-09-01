#coding=utf-8

import MySQLdb
import getpass 


user = raw_input('用户名：')
password = getpass.getpass('密码：')


class Stu(object):
    def to_select(self):
         pass
class Admin(object):
    def to_select(self):
        pass

    def to_insert(self):
        pass

    def to_delete(self):
        pass

    def to_update(self):
         pass

def login():
     pass

def register(db,name,passwd,flog):
    print name,passwd,flog
    cursor = db.cursor()
    result = cursor.execute('select * from login where name="%s"'%(name))
    if result:
        print '该用户已存在'
        cursor.close()
    else:
        try:
            # print name,passwd,flog
            cursor.execute("insert into login (name,passwd,flog) values ('%s','%s','%s')"%(name,passwd,flog))
            db.commit()
            print 'register OK!'
            cursor.close()
        except:
            db.rollback()
            cursor.close()
        
    

def main():
    try:
        db = MySQLdb.connect('localhost',user,password,'testdb')

    except Exception as e:
        print e 

    while True:

        print ''' 
                -----------------Command----------------
                |                 1.login                |
                |                 2.register             |
                |                 3.quit                 |
                |           please select number         |
                ----------------------------------------'''           
        opt = input('your optision >>>')


        if opt == 1:
            print '----Login----'
            lgname = raw_input('Your Login name >>>')
            lgpasswd = getpass.getpass('Your Login passwd >>>')
        elif opt == 2:
            print '----Register----'
            regname = raw_input('Your name >>>')
            regpasswd = getpass.getpass('Your regpasswd >>>')
            # print regpasswd
            id = raw_input('身份(admin/student) >>>')
            if id == 'admin':
                flog = '0'
            elif id == 'student':
                flog = '1'
            register(db,regname,regpasswd,flog)   
        else:
            
            db.close()
            break

if __name__ == '__main__':
    main()