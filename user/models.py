from django.db import models

from MySQLdb import connect
from MySQLdb.cursors import DictCursor
import datetime

# Create your models here.

def insert(name, email, password, sex):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        insert into user values(null, %s, %s, %s, %s, now())
    ''', [name, email, password, sex])
    db.commit()

    cursor.close()
    db.close()

def fetchone(email, password):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        select no, name, email, password, sex
        from user
        where email = %s and password = %s
    ''', [email, password])

    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result

def updateDB(name, email, password, sex):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        update user set
        name = %s, password = %s, sex = %s
        where email = %s
    ''', [name, password, sex, email])
    db.commit()

    cursor.close()
    db.close()

def remove():
    pass

def conn():
    return connect(
        host='192.168.1.33',
        port=3306,
        user='mysite',
        password='976763',
        db='mysite',
        charset='utf8',
    )