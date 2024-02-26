from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomePageView.as_view()),
]

urlpatterns = [
    path('my_app/', views.HomePageView.as_view()),
]
