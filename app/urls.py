from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', show_landing, name='landing'),
    path('join', show_register, name='join'),
    path('search-freelancers', show_freelancers, name="search-freelancers")
]