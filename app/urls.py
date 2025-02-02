
from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListAPIView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView,  ActorRetriveUpdatDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListAPIView.as_view(), name="genre-create-list"),
    path("genres/<int:pk>/", GenreRetrieveUpdateDestroyView.as_view(), name="genre-detail-view"),

    path("actors/", ActorCreateListView.as_view(), name="actors-create-list"),
    path("actors/<int:pk>", ActorRetriveUpdatDestroyView.as_view(), name="actors-detail-view")
]
