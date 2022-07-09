from django.contrib import admin

from photo.models import Album, Photo


# FK연결된 Album,Photo테이블은 1:N관계다. Album 객체를 보여줄 때 연결된 Photo들도 같이 보여줄 수 있다.
# 같이 보여주는 형식은 StackedInline(세로), TabularInline(가로)가 있다. 
class PhotoInLine(admin.StackedInline):
    model = Photo # 추가로 보여주는 테이블
    extra = 2 # 이미 존재하는 개체 외에 추가로 입력할 수 있는 포토 테이블 객체의 수

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInLine,)
    list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')

