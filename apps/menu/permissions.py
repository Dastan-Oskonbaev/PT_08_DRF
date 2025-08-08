from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsActivePost(BasePermission):
    def object_is_archived(self, obj):
        if obj.is_archive == True:
            return obj
        else:
            raise ValidationError("Post is not active")
