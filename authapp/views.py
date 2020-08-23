from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import UserSerializer

class UserProfileView(ProtectedResourceView):

	def get(self, request, *args, **kwargs):
		seri = UserSerializer(request.resource_owner)
		return JsonResponse({'message': 'Profile details.', 'code': 200, 'data': seri.data})


class UserSignupView(APIView):
	
	permission_classes = (AllowAny,)

	def post(self, request, *args, **kwargs):
		seri = UserSerializer(data=request.data)
		if seri.is_valid():
			seri.save()
			return JsonResponse({'message': 'User details added.', 'code': 200})
		error_message = " & ".join([str(seri.errors.get(error)[0]) for error in seri.errors])
		return JsonResponse({'message': 'User details failed to add.', 'code': 200, 'error_detail': error_message})