from django.shortcuts import render, HttpResponse ,redirect

# Create your views here.
def index(request):
    return render(request , "index.html" )

def display(request):
    print(request.POST)
    name_display= request.POST['name']
    location_display = request.POST['location']
    Language_display = request.POST['Language']
    Comment_display= request.POST['Comment']
    content ={ "name" : name_display, 
    'location':location_display,
    'Language':Language_display ,
    'Comment' : Comment_display,

    } 
    return render (request,"result.html" ,content)