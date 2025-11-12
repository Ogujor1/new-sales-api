from rest_framework import permissions


# Read-Only Permission
class IsReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow read-only access.
    Safe methods: GET, HEAD, OPTIONS
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


# Admin or Read-Only Permission
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow:
    - Read access to everyone (GET, HEAD, OPTIONS)
    - Write access only to admin users (POST, PUT, PATCH, DELETE)
    """
    def has_permission(self, request, view):
        # Allow read-only access to everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write access only for admin users
        return request.user and request.user.is_staff


# Authenticated User or Read-Only Permission
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow:
    - Read access to everyone (GET, HEAD, OPTIONS)
    - Write access only to authenticated users (POST, PUT, PATCH, DELETE)
    """
    def has_permission(self, request, view):
        # Allow read-only access to everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write access only for authenticated users
        return request.user and request.user.is_authenticated


# Owner or Read-Only Permission
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow:
    - Read access to everyone (GET, HEAD, OPTIONS)
    - Write access only to the owner of the object
    """
    def has_object_permission(self, request, view, obj):
        # Allow read-only access to everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write access only for the owner
        # Assumes the model has an 'owner' or 'user' field
        return obj.owner == request.user if hasattr(obj, 'owner') else obj.user == request.user
