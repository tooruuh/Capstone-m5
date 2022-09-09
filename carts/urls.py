from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("users/cart/", views.CartView.as_view()),
    path("users/cart/<int:product_id>", views.CartDetailView.as_view()),
]
