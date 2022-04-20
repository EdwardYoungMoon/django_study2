from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark) # 데코레이터 사용하여 admin 사이트에 등록
class BookmarkAdmin(admin.ModelAdmin):
    '''Bookmark 클래스가 Admin 사이트에서 어떻게 보일지 정의'''
    list_display = ('id', 'title', 'url') 


 