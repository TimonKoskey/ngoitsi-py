from django.contrib import admin
from .models import (
	patient_details,
	patient_medical_records,
	payment,
	session
	)

admin.site.register(patient_details)
admin.site.register(patient_medical_records)
admin.site.register(payment)
admin.site.register(session)

