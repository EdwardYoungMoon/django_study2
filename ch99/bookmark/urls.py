from django.urls import path
from bookmark.views import BookmarkDV, BookmarkLV

app_name = 'bookmark' # namespace로 ROOT_URLCONF와 구분하여 충돌 방지
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
