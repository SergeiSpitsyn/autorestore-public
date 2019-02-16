# -*- coding: utf-8 -*-
#from django.conf.urls import url, include
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.services, name='services'),
]
