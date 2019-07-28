"""
file：urls.py
author：陈先生
date：2019/7/2610:24
blog:https://chenpb-lu.github.io
"""
from django.conf.urls import url
from . import views
# app_name = ['question']
urlpatterns = [
    url(r'^detail/$',views.detail),
    url(r'', views.questions, name='questions'),
]