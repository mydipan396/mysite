# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def login(request):
    error_msg = ""
    if request.method == 'POST':
         user = request.POST.get('user', None)
         pwd = request.POST.get('pwd', None)
         if user == 'root' and pwd == '123456':
             return redirect("http://www.baidu.com")
         else:
             error_msg = "用户名或密码错误"
    return render(request, "login.html", {'error_msg':error_msg})
