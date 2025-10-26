from rest_framework.permissions import BasePermission

class IsEnrolled(BasePermission):
    """
    Custom permission to allow access only to users
    who are enrolled in the object (e.g., a course).
    """
    def has_object_permission(self, request, view, obj):
        # Check if the current user is in the object's students
        return obj.students.filter(id=request.user.id).exists()
    

from rest_framework.permissions import BasePermission
class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
