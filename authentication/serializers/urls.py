from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from .views import GetAdministratorDetailsAPIView

urlpatterns = [
    path('admin/auth', obtain_jwt_token),
    path('admin/details', GetAdministratorDetailsAPIView.as_view()),
	]