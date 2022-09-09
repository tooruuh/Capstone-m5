from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("users/login/", views.LoginView.as_view(), name="login-auth-token"),
    path("users/", views.UserView.as_view(), name="user-create"),
]