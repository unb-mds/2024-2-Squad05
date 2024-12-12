from django.contrib import admin
from django.urls import path
from .view.views import *

urlpatterns = [
    path('', index, name='index'),
]
