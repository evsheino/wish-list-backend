from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read permissions for everyone.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write operations only for the owner of the object.
        return obj.user == request.user

class IsAuthenticatedNonOwner(permissions.BasePermission):
    """
    Custom permission to only allow authenticated non-owner users to view or edit the object.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated() and obj.user != request.user
