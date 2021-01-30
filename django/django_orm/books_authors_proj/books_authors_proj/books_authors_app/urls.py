from django.urls import path
from . import views	

# Create your views here.
urlpatterns = [
    path('', views.index),
    path('addBook',views.addBook),
    path('authors',views.authors),
    path('addAuthor',views.addAuthor),
    path('books/<int:book_id>',views.booksView),
    path('authors/<int:Author_id>',views.authorsView),
    path('authors/<int:Author_id>/bookToAuthor',views.add_bookToAuthor),
    path('books/<int:book_id>/AuthorToAbook',views.add_AuthorToAbook)
]