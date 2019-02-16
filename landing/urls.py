# -*- coding: utf-8 -*-
#from django.conf.urls import url, include
from . import views
from django.urls import path, include
from django.views.generic import ListView
from news.models import Article

urlpatterns = [
    path('', views.landing, name='landing'),
    path('', ListView.as_view(queryset=Article.objects.all().order_by("-date")[:2], template_name="landing/page.html")),
]
