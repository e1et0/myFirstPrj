# -*- coding: utf-8 -*-
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone

@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey('auth.User')#аутентификация по юзеру в бд
    titlepr = {'title': 'Заголовок'}
    textpr = {'text': 'Текст'}
    title = models.CharField(titlepr['title'], max_length=200)
    text = models.TextField(textpr['text'])
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publisher(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
