from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated():
            if request.method in SAFE_METHODS:
                return True
            else:
                return request.user.is_staff or request.user.is_superuser