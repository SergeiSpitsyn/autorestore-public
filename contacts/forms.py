# -*- coding: utf-8 -*-
from django import forms
from .models import *

class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        exclude = [""]