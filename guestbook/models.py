from django.db import models
from MySQLdb import connect
from MySQLdb.cursors import DictCursor
import datetime

# Create your models here.
def fetchlist():
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        select  no,
                name,
                password,
                message,
                date_format(date, '%Y-%m-%d %H:%i:%s') as date
        from guestbook
        order by date desc;
    ''')
    results = cursor.fetchall()

    cursor.close()
    db.close()
    return results

def remove(no, password):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        delete from guestbook
        where no = %s and password = %s
    ''', [no, password])
    db.commit()

    cursor.close()
    db.close()

def add(name, password, message):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        insert into guestbook values(null, %s, %s, %s, %s)
    ''', [name, password, message, datetime.datetime.now()])
    db.commit()

    cursor.close()
    db.close()

def conn():
    return connect(
        user='mysite',
        host='192.168.1.33',
        password='976763',
        port=3306,
        charset='utf8',
        db='mysite',
    )