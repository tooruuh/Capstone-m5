from django.urls import path

from . import views

urlpatterns = [
    path("users/cart/", views.CartView.as_view()),
    path("users/<str:cart_id>/cart/buy/", views.CartBuyView.as_view()),
]
