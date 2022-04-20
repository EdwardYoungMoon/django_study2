from django.urls import path
# from bookmark.views import BookmarkDV, BookmarkLV
from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView

app_name = 'bookmark' # namespace로 ROOT_URLCONF와 구분하여 충돌 방지
urlpatterns = [
    path('', ListView.as_view(model=Bookmark), name='index'),
    path('<int:pk>/', DetailView.as_view(model=Bookmark), name='detail'),
]
