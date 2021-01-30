from django.shortcuts import render,redirect
from users.models import User

def index(request):
    context={"User" : User.objects.all() }
    return render( request , 'index.html',context)

def add_user(request):
    User.objects.create(
        first_name = request.POST['firstname'],
        last_name= request.POST['lastname'],
        email_address=request.POST['email'],
        age= int(request.POST['userAge']) )
    return redirect('/')