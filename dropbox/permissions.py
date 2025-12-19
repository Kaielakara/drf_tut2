from rest_framework import permissions

from django.contrib.auth import get_user_model

User = get_user_model

class IsValidPerson(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # print(obj.shared_with)

        if request.user.is_superuser:
            return True

        if request.method == "DELETE":
            if request.user == obj.owner:
                return True

        
        if request.method in permissions.SAFE_METHODS:
            
            if obj.is_public:
                return True
            if obj.shared_with.filter(id=request.user.id).exists() or request.user == obj.owner:
                return True
            
        else:
            if obj.is_locked:
                return False
            
            if obj.shared_with.filter(id=request.user.id).exists() or request.user == obj.owner:
                return True
                

        return False