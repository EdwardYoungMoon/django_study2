from django.contrib import admin

from blog.models import Post

# Register your models here.

@admin.register(Post) # 데코레이터 사용하여 admin 사이트에 등록
class PostAdmin(admin.ModelAdmin): 
    list_display = ('id', 'title', 'modify_dt') # Post 객체를 보여줄 때, id와 title, modify_dt를 출력하라고 지정 
    list_filter = ('modify_dt',) # modify_dt 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
    search_fields = ('title', 'content') # 검색박스를 표시하고, 입력된 단어는 title과 content 컬럼에서 검색하도록 지정
    prepopulated_fields = {'slug' : ('title',)} # slug 필드는 title 필드를 사용해 미리 채워지도록 한다.
    