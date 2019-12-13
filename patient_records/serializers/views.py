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
	)

from .serializers import (
	CreatePatientDetailsSerializer,
	PatientDetailsListSerializer,
	RetrievePatientDetailsSerializer,
	SessionPaymentDetailsSerializer,
	SessionsListSerializer,
	SessionDetailsSerializer,
	SessionDoctorNotesSerializer,
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
		new_state = 'stage one'

		print(session_data)
		patient_obj = patient_details.objects.get(id=int(session_data['patientID']))
		newSessionObj = session(patient=patient_obj, session_state=new_state)
		newSessionObj.save()

		sessionObjSerializer = SessionDetailsSerializer(newSessionObj).data

		return Response(sessionObjSerializer, status=status.HTTP_201_CREATED)

class SessionListAPIView(ListAPIView):
	serializer_class = SessionsListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = session.objects.exclude(session_state='completed')
		return queryset

class GetSessionDetailsAPIView(RetrieveAPIView):
	queryset = session.objects.all()
	serializer_class = SessionDetailsSerializer

class SessionLevelOneAPIView(APIView):
	def post(self, request, *args, **kwargs):
		session_data = request.data
		next_level = 'stage two'

		session_obj = session.objects.get(id=session_data['sessionID'])

		payment_data = {
			'payment_mode': session_data['payment_mode'],
			'payment_method': session_data['payment_method'],
			'amount': session_data['amount'],
			'company_name': session_data['company_name'],
			'mpesa_code': session_data['mpesa_code'],
		}

		payment_serializer = SessionPaymentDetailsSerializer(data = payment_data)
		if payment_serializer.is_valid():
			payment_obj = payment_serializer.create(payment_serializer.validated_data)
			session_obj.payment=payment_obj
			session_obj.session_state=next_level
			session_obj.save()
			sessionObjSerializer = SessionDetailsSerializer(session_obj).data
			return Response(sessionObjSerializer, status=status.HTTP_201_CREATED)
		return Response(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionLevelTwoAPIView(APIView):
	renderer_classes = [JSONRenderer]

	def post(self, request, *args, **kwargs):
		session_data = request.data
		next_level = 'stage three'
		session_obj = session.objects.get(id=session_data['sessionID'])

		patient_medical_records_data = {
			'complaints': session_data['complaints'],
			'investigations': session_data['investigation'],
			'treatment': session_data['treatment'],
		}

		patient_medical_records_serializer = SessionDoctorNotesSerializer(data=patient_medical_records_data)
		if patient_medical_records_serializer.is_valid():
			patient_medical_records_obj = patient_medical_records_serializer.create(patient_medical_records_serializer.validated_data)
			print(patient_medical_records_obj.complaints)
			session_obj.doctor_session = patient_medical_records_obj
			session_obj.session_state=next_level
			session_obj.save()
			sessionObjSerializer = SessionDetailsSerializer(session_obj).data
			print(sessionObjSerializer)
			return Response(sessionObjSerializer, status=status.HTTP_201_CREATED)

		return Response(patient_medical_records_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionFinalLevelAPIView(APIView):
	def post(self, request, *args, **kwargs):
		session_data = request.data
		next_level = 'completed'

		session_obj = session.objects.get(id=session_data['sessionID'])
		session_obj.session_state=next_level
		# session_obj.follow_up_date=session_data['follow_up_date'] if session_data['follow_up_date'] != 'null' else None,

		session_obj.save()

		session_class_serializer = SessionDetailsSerializer(session_obj)

		return Response(session_class_serializer.data, status=status.HTTP_201_CREATED)