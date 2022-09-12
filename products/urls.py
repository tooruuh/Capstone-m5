from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductGenericView.as_view(), name="product-create")
]