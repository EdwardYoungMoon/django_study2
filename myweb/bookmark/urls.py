from django.urls import path
# from bookmark.views import BookmarkDV, BookmarkLV
from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView

from bookmark import views

app_name = 'bookmark' # namespace로 ROOT_URLCONF와 구분하여 충돌 방지
urlpatterns = [
    # path('', ListView.as_view(model=Bookmark), name='index'),
    # path('<int:pk>/', DetailView.as_view(model=Bookmark), name='detail'),

    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),

    #ex) /bookmark/add
    path('add/', views.BookmarkCreateView.as_view(), name='add',),

    #ex) /bookmark/change/
    path('change/', views.BookmarkChangeLV.as_view(), name='change',), 

    #ex) /bookmark/99/update
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update',),

    #ex) /bookmark/99/delete
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete',),
]
