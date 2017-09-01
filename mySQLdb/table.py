#coding=utf-8

import MySQLdb
import getpass 

user = raw_input('用户名：')
password = getpass.getpass('密码：')


try:
    db = MySQLdb.connect('localhost',user,password,'testdb')

except Exception as e:
    print e 

cursor = db.cursor()

sql = '''create table stu(
    id int not null auto_increment primary key,
    name varchar(16) not null,
    age int,
    score float default 0.0
    )'''

cursor.execute(sql)

cursor.close()

db.close()