# this file is created by aman ruhela

from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("",views.index,name='blog_home/index'),
    path("blogpost/<int:id>",views.blogpost,name='blogPOst')
]