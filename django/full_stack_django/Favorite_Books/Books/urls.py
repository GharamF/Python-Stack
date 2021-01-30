from django.urls import path
from . import views

urlpatterns = [
    path('books',views.root),
    path('AddBook', views.AddBook),
    path('books/<int:book_id>', views.viewBook),
    path('<int:book_id>/add_to_Favorite', views.Add_to_fav),
    path('<int:book_id>/add_to_Favorite' , views.Add_to_fav),
    path ('books/<int:book_id>/remove_favorite',views.remove_favorite),
    path ('books/<int:book_id>/update',views.update),
    path ('books/<int:book_id>/delete',views.delete)
    ]