from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    # /blog/ 
    path('', views.PostLV.as_view(), name='index'),

    # /blog/post/
    path('post/', views.PostLV.as_view(), name = 'post_list'),

    # /blog/post/*djnago-example/ 
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # /blog/archive/ ~
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

]
