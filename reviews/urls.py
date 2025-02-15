from django.urls import path
from . import views
# from . import ReviewCreateListView, ReviewRetriveUpdateDestroy

urlpatterns  = [
    path("reviews/", views.ReviewCreateListView.as_view(), name="review-create-list"),
    path("reviews/<int:pk>", views.ReviewRetriveUpdateDestroy.as_view(), name="review-detail-view"),
]