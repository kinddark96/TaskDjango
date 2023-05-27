from django.contrib import admin
from django.urls import path
from course.views import *
urlpatterns = [
    path('', courseList,name=''),
    path('add', courseAdd,name=''),
    path('update/<int:id>',courseUpdate,name='courseUpdate'),
    path('delete/<int:ID>',courseDelete,name='courseDelete'),
]