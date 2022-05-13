from django.contrib import admin
from photo.models import Album, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2
'''외래 키로 연결된 Album, Photo 테이블 간에는 1:N 관계가 성립되므로, 앨범 객체를 보여줄 때
객체에 연결된 사진 객체들을 같이 보여줄 수 있다. 같이 보여주는 형식은 StackedInline과 TabularInline 두 가지가 있다
StackedInline은 세로로 나열되는 형식이다.'''


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')
