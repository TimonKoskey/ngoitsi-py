from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
)

from authentication.models import Administrator
from django.contrib.auth import get_user_model
USER = get_user_model()

class UserDetailsSerializer(ModelSerializer):

	class Meta:
		model = USER
		fields = [
		'username',
		'first_name',
		'last_name',
		'email'
		]

class AdministratorDetailsSerializer(ModelSerializer):
	user = SerializerMethodField()

	class Meta:
		model = Administrator
		fields = [
		'user',
		'is_admin',
		'is_superadmin'
		]

	def get_user(self,obj):
		user = UserDetailsSerializer(obj.user).data
		return user



		