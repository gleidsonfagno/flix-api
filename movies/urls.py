from django.urls import path 
from . import views
# from . import MovieCreateLisView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path("movies/", views.MovieCreateLisView.as_view(), name="movie-create-list"),
    path("movies/<int:pk>", views.MovieRetrieveUpdateDestroyView.as_view(), name="movie-detail-view"),
]