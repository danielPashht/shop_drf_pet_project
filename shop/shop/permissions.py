from rest_framework.permissions import BasePermission


class IsAdminPermission(BasePermission):
    """
    Allows access only to Admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsManagerPermission(BasePermission):
    """
    Allows access only to Manager users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_manager


class IsCustomerPermission(BasePermission):
    """
    Allows access only to Customer users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_customer


class IsOwnerPermission(BasePermission):
    """
    Allows access only to the user who owns the object.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user