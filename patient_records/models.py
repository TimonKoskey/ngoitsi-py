from django.db import models

class PatientDetails(models.Model):
	patient_number = models.IntegerField(blank=True, null=True)
	surname = models.CharField(max_length=50, blank=True, null=True)
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	age = models.CharField(max_length=50, blank=True, null=True)
	sex = models.CharField(max_length=50, blank=True, null=True)
	mobile_number = models.CharField(max_length=50, blank=True, null=True)
	county = models.CharField(max_length=50, blank=True, null=True)
	sub_county = models.CharField(max_length=50, blank=True, null=True)
	village_or_estate = models.CharField(max_length=50, blank=True, null=True)
	post_code = models.CharField(max_length=50, blank=True, null=True)
	address = models.CharField(max_length=50, blank=True, null=True)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return "%s %s %s %d" %(self.surname, self.first_name, self.last_name, self.patient_number)

	class Meta:
		verbose_name_plural = 'Patient Details'

class PatientMedicalRecords(models.Model):
	patient_details = models.ForeignKey(PatientDetails, null=True, blank=True, on_delete=models.CASCADE)
	complaints = models.CharField(max_length=1000, blank=True, null=True)
	investigations = models.CharField(max_length=1000, blank=True, null=True)
	treatment = models.CharField(max_length=1000, blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Patient Medical Records'

class PatientPayment(models.Model):
	patient_details = models.ForeignKey(PatientDetails, null=True, blank=True, on_delete=models.CASCADE)
	payment_method = models.CharField(max_length=50, blank=True, null=True)
	amount = models.CharField(max_length=50, blank=True, null=True)

class PatientSession(models.Model):
	patient = models.ForeignKey(PatientDetails, null=True, blank=True, on_delete=models.CASCADE)
	payment = models.ForeignKey(PatientPayment, null=True, blank=True, on_delete=models.SET_NULL)
	doctor_session = models.ForeignKey(PatientMedicalRecords, null=True, blank=True, on_delete=models.SET_NULL)
	session_date = models.DateField(auto_now_add=True)
	session_starting_time = models.TimeField(auto_now_add=True)
	session_state = models.CharField(max_length=50, blank=True, null=True)
	session_ending_time = models.TimeField(blank=True, null=True)
	follow_up_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return "%s" %(self.patient)

	class Meta:
		verbose_name_plural = 'Sessions'

patient_details = PatientDetails
patient_medical_records = PatientMedicalRecords
payment = PatientPayment
session = PatientSession