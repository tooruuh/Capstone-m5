from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("users/cart/", views.CartView.as_view()),
]
