from django.shortcuts import render, HttpResponse ,redirect
from .models import ninja , dojo


def index(request):
    context={ "Dojos" :  dojo.objects.all()}
    return render(request , "index.html",context)

def new_ninja(request):
    dojo1 = dojo.objects.get( name = request.POST['dojos_name'])
    ninja.objects.create( first_name = request.POST['first_name'] ,last_name= request.POST['last_name'] , dojo_id=dojo1 )
    return redirect('/')


def new_dojo(request):
    dojo.objects.create( name = request.POST['name'] , city=request.POST['city'] , state =request.POST ['State'] )
    return redirect('/')
