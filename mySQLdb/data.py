#coding=utf-8

import MySQLdb
import getpass   # 第三方模块，用来对密码加密

user = raw_input('用户名：')
password = getpass.getpass('密码：')


try:
    # db是对数据库进行打开关闭和生成游标的
    db = MySQLdb.connect('localhost',user,password,'testdb')

except Exception as e:
    print e 

# 游标，用来进行增删改除，用来在数据库里面的操作
cursor = db.cursor()
# print dir(cursor)

# 创建删除表，插入删除数据，更新数据，alter

sql = '''insert into student (name,age,score) values ('lili',20,100)'''

## 只要是对数据进行操作就要
try:
    cursor.execute(sql)
    db.commit()  # 数据提交

except:
    db.rollback()  # 出错要回滚

# 查询到的记录存在cursor对象中,execute是执行sql语句，executemany是执行多条语句
# cursor.execute('select * from student')

# print cursor.description[1][0]  # 返回游标活动状态（一个包含1个元素的元组）

# print cursor.fetchone()   #获取一条语句，具有迭代性质，还有fetchmany(获取指定数量的多条),fetchall
# print cursor.fetchone()

# print cursor.fetchmany(3)  # 为一个3元素的元组

# print cursor.fetchall()

cursor.close()

db.close()