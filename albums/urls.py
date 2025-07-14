from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),  
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('favorite/<int:album_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('my-music/', views.my_music, name='my_music'),
    path('favorites/remove/<int:album_id>/', views.remove_from_favorites, name='remove_from_favorites'),

]
