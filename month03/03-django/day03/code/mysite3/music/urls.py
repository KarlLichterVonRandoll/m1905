"""
    此模块实现music 应用中的子路由配置
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^page1', views.page1_view),
    url(r'^page2', views.page2_view),
    url(r'^page3', views.page3_view),
]
