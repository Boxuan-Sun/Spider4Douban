#!/usr/bin/env python
# coding:utf-8
import sqlite3

# 插入数据
conn = sqlite3.connect("test.db")
print("成功打开数据库")
c = conn.cursor()
sql = '''
    insert into company (id, name, age, address, salary)
    values (1, '张三', 32, '成都', 8000);
'''
c.execute(sql)
conn.commit()
conn.close()
print("数据插入完毕")