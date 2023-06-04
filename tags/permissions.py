from rest_framework import permissions

# BLACKLISTED_IPS = ['127.0.0.1']
# uncomment above to test this permission
BLACKLISTED_IPS = []

class CustomPermission(permissions.BasePermission):
    
    message = 'You are now allowed to view this api since your ip is blocked'
    
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        if ip_addr in BLACKLISTED_IPS:
            return False
        return True