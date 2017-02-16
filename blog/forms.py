# -*- coding: utf-8 -*-
from django import forms
from .models import Post
from django.shortcuts import redirect

class PostForm(forms.ModelForm):

    class Meta:
        model = Post#определение модели для создания формы
        fields = ['title', 'text']#поля для формы
