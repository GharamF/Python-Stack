import bcrypt
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages 


def root(request):
    if request=='POST':
        return redirect('/')
    else:
        return render(request, 'index.html')


def regandlogin(request):
    if request.method =='POST' and request.POST['form'] =='new_user':
        errors = User.objects.user_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
            This_user = User.objects.create(firstname =request.POST['first_name'],
            lastname=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash)
            request.session['user_id']=This_user.id
            return redirect ('/books')
    elif request.method=='POST' and request.POST['form'] =='login':
        errors = User.objects.log_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request, "index.html")
        else:
            user = User.objects.filter(email=request.POST['e-mail']) 
            logged_user = user[0] 
            request.session['user_id']=logged_user.id
            return redirect('/books')
    return redirect("/")


def logout(request):
    request.session.clear()
    return redirect('/')
