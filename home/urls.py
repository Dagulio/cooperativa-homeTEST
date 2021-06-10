
from django.urls import path
from home.views import *
from django.contrib import admin
from django.http import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path(render,home.html),
    path('home/', home)
]