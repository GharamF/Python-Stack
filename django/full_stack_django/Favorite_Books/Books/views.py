import bcrypt
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages 

def root(request):
    if request.session['user_id']:
        context = { 
            'User' : User.objects.get(id= request.session['user_id']) ,
            'books':Books.objects.all()}
        return render (request,"home.html", context )
    else:
        return redirect('/')

def Add_to_fav(request, book_id):
    if request.method=='POST': 
        this_book = Books.objects.get(id = book_id)
        this_user =  User.objects.get(id=request.session['user_id'])
        this_book.users_who_like.add(this_user)
    return redirect('/books')

def AddBook(request):
    if request.method=='POST':
        errors = Books.objects.Book_valdate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            this_user =  User.objects.get(id=request.session['user_id'])
            newFavBook = Books.objects.create( title = request.POST['title'], desc = request.POST['descrption'],uplouded_By = this_user)
            newFavBook.users_who_like.add(this_user)
    return redirect('/books')

def viewBook(request , book_id):
    if request.session['user_id']:
        context = { 
            'Users' : User.objects.all() ,
            'user' : User.objects.get(id=request.session['user_id']),
            'book':Books.objects.get(id = book_id)
            }
        return render (request,"viewBook.html", context )
    else:
        return redirect('/')

def remove_favorite(request , book_id):
    if request.method=='POST': 
        this_book = Books.objects.get(id = book_id)
        User.objects.get(id=request.session['user_id'] ).liked_books.remove(this_book)
    return redirect(f'/books/{book_id}')


def update(request , book_id):
    if request.method=='POST':
        errors = Books.objects.Book_valdate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            book_to_update=Books.objects.get(id = book_id)
            book_to_update.title = request.POST['title']
            book_to_update.desc = request.POST['descrption']
            book_to_update.save()
    return redirect(f'/books/{book_id}')

def delete(request,book_id):
    Books.objects.get(id = book_id).delete()
    return redirect('/books')