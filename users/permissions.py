from rest_framework.permissions import BasePermission
from rest_framework import permissions
class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj
    
class ReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS
    
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
    
