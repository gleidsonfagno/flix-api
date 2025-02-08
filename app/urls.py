
from django.contrib import admin
from django.urls import path, include

from actors.views import ActorCreateListView,  ActorRetriveUpdatDestroyView
from movies.views import MovieCreateLisView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetriveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/v1/", include("genres.urls")),

    path("actors/", ActorCreateListView.as_view(), name="actors-create-list"),
    path("actors/<int:pk>", ActorRetriveUpdatDestroyView.as_view(), name="actors-detail-view"),

    path("movies/", MovieCreateLisView.as_view(), name="movie-create-list"),
    path("movies/<int:pk>", MovieRetrieveUpdateDestroyView.as_view(), name="movie-detail-view"),

    path("reviews/", ReviewCreateListView.as_view(), name="review-create-list"),
    path("reviews/<int:pk>", ReviewRetriveUpdateDestroy.as_view(), name="review-detail-view"),
]
