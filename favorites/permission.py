from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Favorite

class IsUserIsExact(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, favorite: Favorite) -> bool:
        return request.user.id == favorite.user.id