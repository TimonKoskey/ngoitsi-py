from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
)

from patient_records.models import (
	patient_details,
	patient_medical_records,
	payment,
	session,
	)

class CreatePatientDetailsSerializer(ModelSerializer):
	
	class Meta:
		model = patient_details
		fields = [
			'id',
			'patient_number',
			'surname',
			'first_name',
			'last_name',
			'age',
			'sex',
			'mobile_number',
			'county',
			'sub_county',
			'village_or_estate',
			'post_code',
			'address'
		]

	def create(self, validated_data):
		newPatientDetailsOjb = patient_details(
			patient_number = validated_data['patient_number'],
			surname = validated_data['surname'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name'],
			age = validated_data['age'],
			sex = validated_data['sex'],
			mobile_number = validated_data['mobile_number'],
			county = validated_data['county'],
			sub_county = validated_data['sub_county'],
			village_or_estate = validated_data['village_or_estate'],
			address = validated_data['address']
			)
		newPatientDetailsOjb.save()

		return newPatientDetailsOjb

class PatientDetailsListSerializer(ModelSerializer):

	class Meta:
		model = patient_details
		fields = [
			'id',
			'patient_number',
			'surname',
			'first_name',
			'last_name'
		]

class RetrievePatientDetailsSerializer(ModelSerializer):

	class Meta:
		model = patient_details
		fields = [
			'id',
			'patient_number',
			'surname',
			'first_name',
			'last_name',
			'age',
			'sex',
			'mobile_number',
			'county',
			'sub_county',
			'village_or_estate',
			'post_code',
			'address',
			'date_created',
			'last_updated'
		]

class SessionsListSerializer(ModelSerializer):
	patient = SerializerMethodField()
	
	class Meta:
		model = session
		fields = [
			'id',
			'patient',
			'session_state'
		]

	def get_patient(self,obj):
		patient = PatientDetailsListSerializer(obj.patient).data 
		return patient

class SessionPaymentDetailsSerializer(ModelSerializer):

	class Meta:
		model = payment
		fields = [
			'payment_mode',
			'payment_method',
			'amount',
			'company_name',
			'mpesa_code',
		]

	def create(self, validated_data):
		payment_obj = payment(
			payment_mode=validated_data['payment_mode'] if validated_data['payment_mode'] != 'null' else None,
			payment_method=validated_data['payment_method'] if validated_data['payment_method'] != 'null' else None,
			amount=validated_data['amount'] if validated_data['amount'] != 'null' else None,
			company_name=validated_data['company_name'] if validated_data['company_name'] != 'null' else None,
			mpesa_code=validated_data['mpesa_code'] if validated_data['mpesa_code'] != 'null' else None
			)
		payment_obj.save()

		return payment_obj

class SessionDoctorNotesSerializer(ModelSerializer):

	class Meta:
		model = patient_medical_records
		fields = [
			'complaints',
			'investigations',
			'treatment'
		]

	def create(self, validated_data):
		patient_medical_records_obj = patient_medical_records(
			complaints=validated_data['complaints'],
			investigations=validated_data['investigations'],
			treatment=validated_data['treatment'],
			)
		patient_medical_records_obj.save()

		return patient_medical_records_obj

class SessionDetailsSerializer(ModelSerializer):
	patient = SerializerMethodField()
	payment = SerializerMethodField()
	doctor_session = SerializerMethodField()
	
	class Meta:
		model = session
		fields = [
			'id',
			'patient',
			'payment',
			'doctor_session',
			'session_date',
			'session_starting_time',
			'session_ending_time',
			'session_state',
			'follow_up_date',
		]

	def get_patient(self,obj):
		patient = RetrievePatientDetailsSerializer(obj.patient).data 
		return patient

	def get_payment(self,obj):
		payment = SessionPaymentDetailsSerializer(obj.payment).data 
		return payment

	def get_doctor_session(self,obj):
		doctor_session = SessionDoctorNotesSerializer(obj.doctor_session).data 
		return doctor_session
