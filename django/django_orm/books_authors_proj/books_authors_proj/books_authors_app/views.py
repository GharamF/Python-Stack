from django.shortcuts import render, redirect,HttpResponse
from .models import Books , Authors

#main

def index(request):
    context = {'Books' : Books.objects.all() }
    return render(request , 'index.html' , context)

def authors(request):
    context = {'Authors' : Authors.objects.all() }
    return render(request , 'authors.html' , context)

#view 

def booksView(request , book_id):
    context = { 'Books' : Books.objects.get(id = book_id),
    'Authors' : Authors.objects.all()
    }
    return render(request , 'booksView.html' , context)

def authorsView(request , Author_id):
    context = { 'Authors' : Authors.objects.get(id = Author_id),
    'Books' : Books.objects.all()
    }
    return render(request , 'authorsView.html' , context)

# Add 

def addBook(request):
    Books.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect ('/')

def addAuthor(request):
    Authors.objects.create(first_name=request.POST['Fname'], last_name=request.POST['lname'],notes=request.POST['notes'])
    return redirect ('/authors')

# Add To
def add_AuthorToAbook(request ,book_id):
    author1=Authors.objects.get(id=request.POST['Authors_name'])
    Books.objects.get(id=book_id).authors.add(author1)
    return redirect('/')

def add_bookToAuthor(request ,Author_id):
    book=Books.objects.get(id=request.POST['Books_name'])
    Authors.objects.get(id = Author_id).book.add(book)
    return redirect('/authors')