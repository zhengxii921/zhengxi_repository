from django.urls import path
from . import views


app_name = "numazutourist"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("reviews", views.ReviewListView.as_view(), name="reviews"),
    path("places", views.PlaceListView.as_view(), name="places"),
    path("add_place", views.PlaceCreateView.as_view(), name="add_place"),
]

