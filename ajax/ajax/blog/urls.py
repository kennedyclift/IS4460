from django.contrib import admin
from django.urls import include, path

from blog import views

urlpatterns = [
    path("list/", views.get_posts,name="get_posts")
]