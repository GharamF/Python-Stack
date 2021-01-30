from django.shortcuts import render ,redirect 
from .models import tvshow
from django.contrib import messages
# Create your views here.

def index(request):
    return redirect('/shows')

def viewtvshow(request):
    context = {'tvshows' : tvshow.objects.all() }
    return render (request , 'index.html', context)

def index2(request):
    return render(request,'add_show.html')

def add_show(request):
    errors = tvshow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new/')
    else:
        tvshow.objects.create(title= request.POST['title'] ,network=request.POST['network'] , releasedate=request.POST['releasedate'], descrption=request.POST['descrption'])
        messages.success(request, "tvshow successfully updated")
        return ('/shows/new/')


def index3(request , show_id):
    context = {'tvshow': tvshow.objects.get(id=show_id) }
    return render(request,'edit_show.html',context)

def edit_show(request , show_id):
    errors = tvshow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        tvshow_to_update =tvshow.objects.get(id=show_id)
        tvshow_to_update.title=request.POST['title']
        tvshow_to_update.network=request.POST['network']
        tvshow_to_update.releasedate=request.POST['releasedate']
        tvshow_to_update.descrption=request.POST['descrption']
        tvshow_to_update.save()
        return redirect('/')


def showTvShow(request , show_id):
    context = { 'tvshow': tvshow.objects.get(id=show_id) }
    return render(request,'show_tvshow.html',context)

def delete_show(request,show_id):
    tvshow.objects.get(id=show_id).delete()
    return redirect('/')
