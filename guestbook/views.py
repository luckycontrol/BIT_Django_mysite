from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from guestbook.models import fetchlist, remove, add
# Create your views here.
def list(request):
    results = fetchlist()
    data = {'guestbook' : results}
    return render(request, 'guestbook/list.html', data)

def deleteform(request):
    return render(request, 'guestbook/deleteform.html')

def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    remove(no, password)
    return HttpResponseRedirect('/guestbook/list')

def insert(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    add(name, password, message)
    return HttpResponseRedirect('/guestbook/list')