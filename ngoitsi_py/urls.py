from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('patients-records/',include('patient_records.serializers.urls')),
    path('authentication/',include('authentication.serializers.urls')),
]
