from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie-list'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('add/', views.MovieCreateView.as_view(), name='movie-add'),
    path('<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie-delete'),
]
