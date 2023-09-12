from rest_framework import permissions


class IsSeller(permissions.BasePermission):

    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            return request.user.type == 'SELLER'
        else:
            return False
