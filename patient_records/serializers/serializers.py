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

class SessionDetailsSerializer(ModelSerializer):
	patient = SerializerMethodField()
	
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
