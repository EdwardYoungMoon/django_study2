from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView 


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    
    # APP_URLCONF
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),

    #class-based views
    #path('bookmark/',  BookmarkLV.as_view(), name = 'index'),
    #path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
