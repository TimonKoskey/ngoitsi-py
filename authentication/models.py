from django.db import models

from django.contrib.auth import get_user_model
USER = get_user_model()

class Administrator(models.Model):
	user = models.OneToOneField(USER, null=True, blank=True, on_delete=models.CASCADE)
	is_admin = models.BooleanField(null=True, blank=True)
	is_superadmin = models.BooleanField(null=True, blank=True)

	def __str__(self):
		return "%s" %(self.user)

	class Meta:
		verbose_name_plural = 'Administrators'
