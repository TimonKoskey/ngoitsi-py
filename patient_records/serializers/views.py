from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from datetime import datetime

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
	session_one,
	session_two,
	session_three,
	)

from .serializers import (
	CreatePatientDetailsSerializer,
	PatientDetailsListSerializer,
	RetrievePatientDetailsSerializer,
	SessionPaymentDetailsSerializer,
	SessionsListSerializer,
	SessionDetailsSerializer,
	SessionDoctorNotesSerializer,
	SessionOneSerializer,
	SessionTwoSerializer,
	SessionThreeSerializer
	)

class CreatePatientDetailsAPIView(APIView):

	def post(self, request, *args, **kwargs):
		patient_data = request.data
		patient_data_serializer = CreatePatientDetailsSerializer(data=patient_data)

		if patient_data_serializer.is_valid():
			patient_details_obj = patient_data_serializer.create(patient_data_serializer.validated_data)
			patient_details_obj_serializer = CreatePatientDetailsSerializer(patient_details_obj)

			return Response(patient_details_obj_serializer.data, status=status.HTTP_201_CREATED)

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
		state = 'running'

		patient_obj = patient_details.objects.get(id=int(session_data['patientID']))
		session_qs = session.objects.filter(patient = patient_obj)
		for obj in session_qs:
			if obj.session_state == 'running':
				return Response('RUNNING SESSION WITH SIMILAR CREDENTIALS', status=status.HTTP_400_BAD_REQUEST)
		newSessionObj = session(patient=patient_obj, session_state=state)
		newSessionObj.save()

		sessionObjSerializer = SessionDetailsSerializer(newSessionObj).data

		return Response(sessionObjSerializer, status=status.HTTP_201_CREATED)

class SessionListAPIView(ListAPIView):
	serializer_class = SessionsListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = session.objects.filter(session_state='running')
		return queryset

class GetSessionDetailsAPIView(RetrieveAPIView):
	queryset = session.objects.all()
	serializer_class = SessionDetailsSerializer

class EndSessionAPIView(APIView):

	def post(self, request, *args, **kwargs):
		session_data = session_data = request.data
		session_obj = session.objects.get(id=session_data['sessionId'])

		sessionOne_obj = session_one(
			session=session_obj
			)
		sessionOneData = session_data['sessionOne']
		sessionPaymentData = sessionOneData['paymentInformation']
		sessionPaymentSerializer = SessionPaymentDetailsSerializer(data=sessionPaymentData)
		if not sessionPaymentSerializer.is_valid():
			return Response(sessionPaymentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

		payment_obj = sessionPaymentSerializer.create(sessionPaymentData)
		sessionOne_obj.is_completed=True
		sessionOne_obj.save()

		sessionTwo_obj = session_two(
			session=session_obj
			)
		sessionTwoData = session_data['sessionTwo']
		patientMedicalRecordData = sessionTwoData['medical_information']
		patientMedicalRecordSerializer = SessionDoctorNotesSerializer(data=patientMedicalRecordData)
		if not patientMedicalRecordSerializer.is_valid():
			return Response(patientMedicalRecordSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

		medicalRecordObj = patientMedicalRecordSerializer.create(patientMedicalRecordData)
		sessionTwo_obj.is_completed=True
		sessionTwo_obj.save()

		sessionThree_obj = session_three(
			session=session_obj,
			follow_up_date=session_data['sessionThree']['follow_up_date'],
			is_completed=True
			)
		sessionThree_obj.save()

		session_obj.session_state = 'complete'
		session_obj.save()

		return Response(status=status.HTTP_201_CREATED)

