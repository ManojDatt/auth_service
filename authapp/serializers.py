from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password', 'is_active', )

	def validate_password(self, value: str) -> str:
		return make_password(value)