from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductGenericView.as_view(), name="product-view"),
    path(
        "products/<str:product_id>/",
        views.ProductDetailView.as_view(),
        name="product-detail",
    ),
    path("products/search/", views.ProductSearchView.as_view(), name="product-search"),
]
