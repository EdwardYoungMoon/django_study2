from ast import Add
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField('TITLE', max_length= 100)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    desciption = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE_DT', auto_now_add= True)
    modify_dt = models.DateTimeField('MODIFY_DT', auto_now = True)
    
    class Meta: # 필드 속성 외에 필요한 파라미터가 있으면 Meta 내부 클래스로 정의한다.
        verbose_name = 'post' # 테이블의 단수 별칭
        verbose_name_plural = 'posts' # 테이블의 복수 별칭
        db_table = 'blog_post' # DB에 저장되는 테이블의 이름을 blog_post로 지정. 
        ordering = ('-modify_dt',) # 모델 객체의 리스트 출력 시 modify_dt 컬럼을 기준으로 내림차순으로 정렬

    def __str__(self):
        return self.title

    def get_absolute_url(self): # 이 메소드가 정의된 객체를 지칭하는 URL 반환. 
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self): # 내장함수 호출. modify_dt 컬럼을 기준으로 최신 포스트 반환
        return self.get_previous_by_modify_dt()
    
    def get_next(self): # 내장함수 호출. modify_dt 컬럼을 기준으로 예전 포스트 반환
        return self.get_absolute_by_modify_dt()

    
    
