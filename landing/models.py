# -*- coding: utf-8 -*-
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)