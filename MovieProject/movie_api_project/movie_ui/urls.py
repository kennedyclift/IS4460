from django.urls import path
from . import views

urlpatterns = [
    path('movie-list/', views.movie_list, name='movie-list'),
    path('movie-details/<int:movie_id>/', views.movie_details, name='movie-details'),
    path('movie-add/', views.movie_add, name='movie-add'),
    path('movie-update/<int:movie_id>/', views.movie_update, name='movie-update'),
    path('movie-delete/<int:movie_id>/', views.movie_delete, name='movie-delete'),
]
