from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from department import forms, views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
