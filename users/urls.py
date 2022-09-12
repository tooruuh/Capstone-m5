from django.urls import path
from . import views

urlpatterns = [
    path("users/login/", views.LoginView.as_view(), name="login-auth-token"),
    path("users/", views.UserView.as_view(), name="user-create"),
    path("users/<str:user_id>/", views.UpdateView.as_view(), name="user-update")
]