# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import MailForm


def contacts(request):
    name = "Grey"
    current_day = "27.01.2019"
    form = MailForm(request.POST or None)

    if request.method == "POST":
#        print(form)
        print(request.POST)

    return render(request, 'contacts/page.html', locals())

