from django.urls import path
from .views import *
urlpatterns = [
    path('', traineeList,name=''),
    path('add', traineeAddFrom,name=''),
    path('update/<int:id>',traineeUpdateModelForm,name='traineeUpdate'),
    path('delete/<int:ID>',traineeDelete,name='traineeDelete'),
]