#file:sport/urls.py
"""
此模块实现sport应用中的子路由配置
"""
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^index',views.index_view),
]