from rest_framework import permissions
from rest_framework.views import Request, View
from products.models import Product


class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
    
class IsSellerIsExact(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, product: Product) -> bool:
        print(product)
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == product.seller_id or request.user.is_superuser