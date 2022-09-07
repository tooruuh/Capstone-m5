from rest_framework import permissions
from rest_framework.views import Request, View

from .models import User

SAFE_METHODS = ('POST', 'HEAD', 'OPTIONS')

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
