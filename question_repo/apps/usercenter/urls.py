"""
file：urls.py
author：陈先生
date：2019/7/2610:24
blog:https://chenpb-lu.github.io
"""
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^profile/$', views.profile),
]