from django.urls import path
from . import views

urlpatterns = [
    path("users/login/", views.LoginView.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<str:user_id>/", views.UpdateView.as_view()),
]