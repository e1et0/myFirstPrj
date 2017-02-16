# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):#все записи
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')#QuerySet
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):#получаем одну запись
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):#создание новой записи
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_del(request, pk):#удаление записи
    Post.objects.get(pk=pk).delete()
    return redirect('blog.views.post_list')

def post_update(request, pk):#обновление записи
    postupd = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=postupd)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            form.save()
            return redirect('blog.views.post_detail', pk=pk)
    else:
        form = PostForm(instance=postupd)
    return render(request, 'blog/post_edit.html', {'form': form})
            
       

        
    
        
