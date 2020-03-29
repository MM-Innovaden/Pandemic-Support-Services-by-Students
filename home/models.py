from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Outcome(models.Model):
	description = models.CharField(max_length=70)

	class Meta:
		ordering = ['description']

	def __str__(self):
		return self.description

class Patient(models.Model):
	# Model for patients
	name = models.CharField(max_length=200)
	age = models.PositiveSmallIntegerField()
	address = models.TextField()
	phone_number = models.CharField(max_length=10)
	date_contacted = models.DateField()
	contacted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	outcome = models.ForeignKey(Outcome, on_delete=models.PROTECT)

	class Meta:
		ordering = ['date_contacted']
		permissions = (("is_staff", "Has the staff permissions"),) 

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('patient-detail', args=[str(self.id)])

