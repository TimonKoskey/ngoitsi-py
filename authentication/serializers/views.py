from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# from rest_framework_jwt.views import ObtainJSONWebToken
# from datetime import datetime
# from rest_framework_jwt.settings import api_settings

from rest_framework.generics import (
	RetrieveAPIView,
	)

from .serializers import (
	UserDetailsSerializer,
	AdministratorDetailsSerializer
	)

from authentication.models import Administrator
from django.contrib.auth import get_user_model

# jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
USER = get_user_model()


class GetAdministratorDetailsAPIView(APIView):

	def get(self, request, *args, **kwargs):
		user = request.user 
		admin_obj = Administrator.objects.get(user=user)
		adminObjSerializer = AdministratorDetailsSerializer(admin_obj).data
		return Response(adminObjSerializer, status=status.HTTP_200_OK)