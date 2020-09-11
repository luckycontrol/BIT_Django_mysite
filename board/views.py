from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from board.models import fetchlist, fetch_board, get_max_g_no, get_max_o_no, get_max_depth, add

# Create your views here.
def list(request):
    page_no = request.GET['page_no']
    data = fetchlist(page_no)
    board_data = {'board_list': data[0], 'board_count': data[1]}

    return render(request, 'board/list.html', board_data)

def write(request):
    return render(request, 'board/write.html')

def view(request):
    no = request.GET['no']
    data = fetch_board(no)
    board_data = {'board_list': data}
    return render(request, 'board/view.html', board_data)

def modify(request):
    return render(request, 'board/modify.html')

def delete(request):
    pass

def insert(request):
    title = request.POST['title']
    content = request.POST['content']
    author = request.POST['author']
    g_no = request.POST['g_no']
    o_no = request.POST['o_no']
    user_no = request.POST['user_no']

    # 새 글을 작성하고자 할 때
    if g_no == '':
        g_no, o_no, depth = get_max_g_no(), 1, 1

    # 댓글 달 때
    elif int(o_no) == 1:
        g_no, o_no, depth = g_no, get_max_o_no(g_no), get_max_depth(g_no, o_no)

    # 대댓글 달 때
    elif int(o_no) > 1:
        g_no, o_no, depth = g_no, o_no, get_max_depth(g_no, o_no)

    add(title, content, author, g_no, o_no, depth, user_no)

    return HttpResponseRedirect('/board/list?page_no=1')