from django.urls import path, include
from .views import ListCreateMovieView, MovieDetailView


urlpatterns = [
    path('movies/', ListCreateMovieView.as_view(), name="movies-list-create"),
    path('movies/<slug:pk>/', MovieDetailView.as_view(), name="movies-detail")
]
