from django.urls import path

from . import views

urlpatterns = [
    path("users/favorite/", views.FavoriteView.as_view(), name="favorite-view"),
    path(
        "users/favorite/<str:favorite_id>/",
        views.FavoriteDetailView.as_view(),
        name="favorite-details",
    ),
]
