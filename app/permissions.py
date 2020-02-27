from rest_framework.permissions import BasePermission


class IsAllowedToModify(BasePermission):
    """
    Restrict volunteer permission to respective college.
    """

    def has_object_permission(self, request, view, student):
        return student.college == request.user.volunteerprofile.college
