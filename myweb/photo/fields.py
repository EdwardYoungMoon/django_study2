'''
장고의 기본 필드 외에 개발자가 스스로 만드는 필드를 커스텀 필드라고 한다. 
'''

import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile 


class ThumbnailImageFieldFile(ImageFieldFile): # 파일시스템에 직접 파일을 쓰고 지우는 작업
    def _add_thumb(self, s):
        parts = s.split('.')
        parts.insert(-1, 'thumb')
        if parts[-1].lower() not in ['jpeg', 'jpg']:
            parts[-1] = 'jpg'
        return '.'.join(parts)

    @property  # property 데코레이터를 사용하면, 메소드를 멤버변수처럼 사용할 수 있다.
    def thumb_path(self): #이미지를 처리하는 필드는 파일의 경로와 url 속성을 제공해야 한다. 원본 파일의 경로인 path 속성에 추가해, 썸네일의 경로인 thumb_path 속성을 만든다. 
        return self._add_thumb(self.path)
    

    @property
    def thub_url(self): #원본파일의 url속성에 추가해, 썸네일의 URL인 thumb_url 속성을 만든다. 
        return self._add_thumb(self.url) 

    def save(self, name, content, save=True): #파일을 저장하고 생성하는 메소드
        super().save(name, content, save) #부모 ImageFieldFile클래스의 save() 메소드를 호출해 원본 이미지를 저장한다.

        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        background = Image.new('RGB', size, (255,255,255))
        box = (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)) #정사각형 모양의 썸네일 이미지를 만든다.
        background.paste(img, box)
        background.save(self.thumb_path, 'JPEG') #합쳐진 최종 이미지를 JPEG 형식으로 thumb_path 경로에 저장

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField): 
    attr_class = ThumbnailImageFieldFile # 새로은 FileField 클래스를 정의할 때는 그에 상응하는 File 처리 클래스를 속성에 지정

    def __init__(self, verbose_name=None, thumb_width = 128, thumb_height = 128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)




