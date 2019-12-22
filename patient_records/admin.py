from django.contrib import admin
from .models import (
	patient_details,
	patient_medical_records,
	payment,
	session,
	session_one,
	session_two,
	session_three,
	)

admin.site.register(patient_details)
admin.site.register(patient_medical_records)
admin.site.register(payment)
admin.site.register(session)
admin.site.register(session_one)
admin.site.register(session_two)
admin.site.register(session_three)

