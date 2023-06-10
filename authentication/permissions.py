from rest_framework import permissions
from authentication.models import User

class IsAuthenticated(permissions.BasePermission):
    
    message = 'Invalid user access found'
    
    def has_permission(self, request, view):
        user = request.user
        return isinstance(user, User)

class IsAdmin(permissions.BasePermission):
    
    message = 'Only admin access is allowed here'
    
    def has_permission(self, request, view):
        user = request.user 
        return user.is_superuser
