from django.http import HttpResponseRedirect
from django.shortcuts import render

from user.models import insert, fetchone, updateDB

# Create your views here.
def loginform(request):
    return render(request, 'user/loginform.html')

def joinform(request):
    return render(request, 'user/joinform.html')

def join(request):
    name = request.POST['name']
    password = request.POST['password']
    email = request.POST['email']
    gender = request.POST['gender']

    insert(name, email, password, gender)

    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    result = fetchone(email, password)

    if result is None:
        return HttpResponseRedirect('/user/loginform?result=fail')

    request.session['authuser'] = result
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authuser']

    return HttpResponseRedirect('/')

def updateform(request):
    result = fetchone(request.session['authuser']['email'], request.session['authuser']['password'])
    data = {'user': result}

    return render(request, 'user/updateform.html', data)

def update(request):
    no = request.POST['no']
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    sex = request.POST['sex']

    updateDB(name, email, password, sex)

    request.session['authuser'] = {'no': no, 'name': name, 'email': email, 'password': password, 'sex': sex}

    return HttpResponseRedirect('/user/updateform')