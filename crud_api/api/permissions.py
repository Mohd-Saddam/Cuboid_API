from rest_framework import permissions
from django.contrib.auth.models import User
from django.conf import settings

# user = settings.AUTH_USER_MODEL()


class IsAuthenticated(permissions.BasePermission):

	def has_permission(self, request, obj):
		return request.user.is_authenticated

class IsStaff(permissions.BasePermission):

	def has_permission(self, request, obj):
		return request.user.is_staff

class IsOwner(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		return obj.created_by == request.user

