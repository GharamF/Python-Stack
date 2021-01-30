from django.urls import path
from . import views	

# Create your views here.
urlpatterns = [
    path('', views.index),
    path('shows',views.viewtvshow),
    path('shows/new/',views.index2),
    path('shows/new/add_show',views.add_show),
    path('<int:show_id>/edit',views.index3),
    path('shows/<int:show_id>/edit',views.index3),
    path('<int:show_id>/delete',views.delete_show),
    path('shows/<int:show_id>',views.showTvShow),
    path('<int:show_id>/editShow',views.edit_show),
    path('shows/<int:show_id>/delete',views.delete_show),
]