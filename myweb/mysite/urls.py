from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView 

from django.conf.urls.static import static
from django.conf import settings

from mysite.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'), #계정 생성이 완료됐다는 메시지
    
    # APP_URLCONF
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),

    path('photo/', include('photo.urls')),

    #class-based views
    #path('bookmark/',  BookmarkLV.as_view(), name = 'index'),
    #path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #기존URL 패턴에 static 함수가 반환하는 패턴 추가 
# static(prefix, view=django.views.static.serve, **kwargs)
