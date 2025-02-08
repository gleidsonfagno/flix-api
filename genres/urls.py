from django.urls import path
from genres.views import  GenreCreateListAPIView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreCreateListAPIView.as_view(), name="genre-create-list"),
    path("genres/<int:pk>/", GenreRetrieveUpdateDestroyView.as_view(), name="genre-detail-view"),
]