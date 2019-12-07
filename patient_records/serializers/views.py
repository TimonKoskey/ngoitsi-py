from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import (
	CreateAPIView,
	# RetrieveUpdateAPIView,
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView
	)

from patient_records.models import (
	patient_details,
	patient_medical_records,
	payment,
	session,
	)

from .serializers import (
	CreatePatientDetailsSerializer,
	PatientDetailsListSerializer,
	RetrievePatientDetailsSerializer,
	SessionsListSerializer,
	SessionDetailsSerializer
	)

class CreatePatientDetailsAPIView(APIView):

	def post(self, request, *args, **kwargs):
		patient_data = request.data
		patient_data_serializer = CreatePatientDetailsSerializer(data=patient_data)

		if patient_data_serializer.is_valid():
			patient_details_obj = patient_data_serializer.create(patient_data_serializer.validated_data)

			return Response(patient_data_serializer.data, status=status.HTTP_201_CREATED)

		return Response(patient_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientsListAPIView(ListAPIView):
	serializer_class = PatientDetailsListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = patient_details.objects.all()
		return queryset

class GetPatientDetailsAPIView(RetrieveAPIView):
	queryset = patient_details.objects.all()
	serializer_class = RetrievePatientDetailsSerializer

class UpdatePatientDetailsAPIView(UpdateAPIView):
	queryset = patient_details.objects.all()
	serializer_class = RetrievePatientDetailsSerializer

class DeletePatientDetailsAPIView(DestroyAPIView):
	queryset = patient_details.objects.all()
	serializer_class = RetrievePatientDetailsSerializer

class StartNewSessionAPIView(APIView):
	def post(self, request, *args, **kwargs):
		session_data = request.data
		next_level = 'stage one'

		print(session_data)
		pass

class SessionListAPIView(ListAPIView):
	serializer_class = SessionsListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = session.objects.exclude(session_state='completed')
		return queryset

class SessionLevelOneAPIView(APIView):
	def post(self, request, *args, **kwargs):
		session_data = request.data
		next_level = 'stage two'
		pass

class SessionLevelTwoAPIView(APIView):
	def post(self, request, *args, **kwargs):
		session_data = request.data
		next_level = 'stage three'
		pass

class SessionFinalLevelAPIView(APIView):
	def post(self, request, *args, **kwargs):
		session_data = request.data
		next_level = 'completed'
		pass
