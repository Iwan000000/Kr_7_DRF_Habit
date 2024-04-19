from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Разрешение на проверку владельца"""
    message = "Вы не владелец"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsUser(BasePermission):
    """Разрешение на проверку пользователя"""
    message = "Вы не владелец"

    def has_object_permission(self, request, view, obj):
        return request.user == obj
