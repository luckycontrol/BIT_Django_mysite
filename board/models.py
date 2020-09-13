from django.db import models

from MySQLdb import connect
from MySQLdb.cursors import DictCursor

# Create your models here.

# 게시판 리스트를 가져온다.
def fetchlist(num):
    db = conn()
    cursor = db.cursor(DictCursor)

    pages = (int(num) - 1) * 5

    cursor.execute('''
        select * from board
        order by g_no desc, o_no asc
        limit %s, 5
    ''', [pages])
    board_list = cursor.fetchall()

    cursor.execute('''
        select count(*) as count from board
    ''')
    board_count = cursor.fetchone()     # 총 게시물 수
    top_board_no = board_count['count'] - (int(num) - 1) * 5  # n번째 페이지의 맨 상단 게시물 번호
    board_count_range = range(1, board_count['count'] // 5 + 2)     # 하단 페이지 인덱스들

    cursor.close()
    db.close()

    return [board_list, top_board_no, list(board_count_range)]

# 게시판 게시물을 클릭했을 때, 해당 게시물의 내용을 가져온다.
def fetch_board(no):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        select * from board
        where no = %s
    ''', [no])

    result = cursor.fetchone()

    cursor.close()
    db.close()
    return result

# g_no 최대 구하기
def get_max_g_no():
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        select max(g_no) as g_no from board
    ''')
    result = cursor.fetchone()

    cursor.close()
    db.close()

    if result['g_no'] is None:
        return 1
    else:
        return result['g_no'] + 1

# o_no 최대 구하기
def get_max_o_no(g_no):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        select max(o_no) as o_no from board
        where g_no = %s
    ''', [g_no])

    result = cursor.fetchone()

    cursor.close()
    db.close()
    return result['o_no'] + 1

# depth 최대 구하기
def get_max_depth(g_no, o_no):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        select max(depth) as depth from board
        where g_no = %s and o_no = %s
    ''', [g_no, o_no])
    result = cursor.fetchone()

    cursor.close()
    db.close()
    return result['depth'] + 1

def add(title, content, author, g_no, o_no, depth, user_no):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        insert into board values(null, %s, %s, %s, 0, now(), %s, %s, %s, %s)          
    ''', [title, content, author, g_no, o_no, depth, user_no])
    db.commit()

    cursor.close()
    db.close()

# 조회수 업데이트
def update_view_count(no, view_count):
    db = conn()
    cursor = db.cursor(DictCursor)

    cursor.execute('''
        update board set view = %s
        where no = %s;
    ''', [int(view_count) + 1, no])
    db.commit()

    cursor.close()
    db.close()

def conn():
    return connect(
        host='192.168.1.33',
        port=3306,
        db='mysite',
        user='mysite',
        password='976763',
        charset='utf8',
    )

# select * from board order by g_no desc, o_no asc limit (page-1) * 5, 5