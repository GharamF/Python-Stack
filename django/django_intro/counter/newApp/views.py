from django.shortcuts import render , redirect


# Create your views here.
def index(request):
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter + 1
    context = {'counter': counter }
    return render(request,'index.html',context)

def destroy_session(request):
    del request.session['counter'] 
    return redirect('/')

def add_two(request):
    request.session['counter'] += 1
    return redirect('/')

def increment_by(request):
    request.session['counter'] += int(request.POST['num'])
    return redirect('/')