from django.shortcuts import render, HttpResponse ,redirect
from time import gmtime, strftime

# Create your views here.
def display(request):
    context = {
        "time": strftime(" %b %d ,%Y  %H:%M %p", gmtime())
    }
    return render(request, "index.html" ,context)