from django.urls import path
from .views import *
urlpatterns = [
    path('', traineeList,name=''),
    path('add', traineeAdd,name=''),
    path('update/<int:id>',traineeUpdate,name='traineeUpdate'),
    path('delete/<int:ID>',traineeDelete,name='traineeDelete'),
]