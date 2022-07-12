from operator import mod
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from django.contrib.auth.models import User
from django.utils.text import slugify # slugify()함수는 원래 단어를 알파벳 소문자, 숫자, 밑줄, 하이픈으로만 구성된 단어로 만들어준다.

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alais.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True) 
    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name= 'OWNER', blank=True, null=True)


    # 필드 속성 외에 필요한 파라미터가 있으면 Meta 내부 클래스로 정의.
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self) -> str:
        return self.title

    
    # def get_absolute_url(self):
    #     return reverse('blog: post_detail', args=(self.slug))
    def get_absolute_url(self): # 이 메소드가 정의된 객체를 지칭하는 URL 반환. 
        return reverse('blog:post_detail', args=(self.slug,))

    # modify_dt 컬럼을 기준으로 최신 포스트를 반환
    def get_previous(self):
        return self.get_previous_by_modify_dt()

    # -modify_dt 컬럼을 기준으로 예전 포스트를 반환
    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True) # save메소드 제정의.
        super().save(*args, **kwargs)




    

