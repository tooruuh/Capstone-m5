from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User

SAFE_METHODS = ('POST', 'HEAD', 'OPTIONS')

class IsSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True

class IsUserIsExact(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        return request.user.id == user.id

