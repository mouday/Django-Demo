# -*- coding: utf-8 -*-
from django.urls import path
from . import views

# 添加命名空间
app_name = "myblog"

urlpatterns = [
    path('hello', views.hello),
    path('articles', views.articles),
    path('index', views.index_page, name="index"),
    path('detail/<int:article_id>', views.detail_page, name="detail"),
]
