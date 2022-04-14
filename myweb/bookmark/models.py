from pickle import _BufferCallback
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=200, blank=True)
    url = models.URLField('URL', unique=True) # URL == verbose_name(별칭)

    def __str__(self) -> str:
        return self.title