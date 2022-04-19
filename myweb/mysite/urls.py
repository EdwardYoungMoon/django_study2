from unicodedata import name
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # APP_URLCONF
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),

    #class-based views
    #path('bookmark/',  BookmarkLV.as_view(), name = 'index'),
    #path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
