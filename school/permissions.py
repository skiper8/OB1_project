from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """ Permissions class для пользователей с флагом is_staff """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
