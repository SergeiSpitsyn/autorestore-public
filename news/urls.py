# -*- coding: utf-8 -*-
from django.urls import path, include
from django.views.generic import ListView, DetailView
from news.models import Article

urlpatterns = [
    path('', ListView.as_view(queryset=Article.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    path('<int:pk>', DetailView.as_view(model=Article, template_name="news/post.html")),
]
