from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    # Ex : /photo/
    path('', views.AlbumLV.as_view(), name='index'),
    
    # Ex : /photo/album/, same as /photo/
    path('album/', views.AlbumLV.as_view(), name='album_list'),

    # Ex : /photo/album/99
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # Ex : /photo/photo/99
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
]
