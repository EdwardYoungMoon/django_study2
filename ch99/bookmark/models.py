from operator import mod
from django.db import models

# Create your models here.

# 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은 클래스의 변수로 매핑
# 테이블 클래스는 django.db.models.Model 클래스를 상속받아 정의

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return self.title


