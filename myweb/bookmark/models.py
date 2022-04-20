from django.db import models

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=200, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self) -> str:
        return self.title

    