from django.db import models

from django.contrib.auth.models import User

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=200, blank=True)
    url = models.URLField('URL', unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) #

    def __str__(self) -> str:
        return self.title

    