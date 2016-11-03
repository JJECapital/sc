from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

class Job(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	salary = models.IntegerField()
	company = models.CharField(max_length=64, default='<undisclosed>')
	url = models.URLField(default='<no url>')
	SECURITY_CLEARANCE_CHOICES = (
		('DV', 'Developed Vetting (DV)'),
		('SC', 'Security Check (SC)'),
		('BPSS', 'Baseline Personnel Security Standard (BPSS)'),
		('CTC', 'Counter Terrorist Check (CTC)'),
		('NATO', 'NATO Cleared (NR/NC/NS/CTS)'),
		('MPS', 'Metropolitan Police Service (MPS:IVC/MV)'),
		('SIA', 'Security Industry Authority (SIA)'),
		('DBS/EDBS', '[Enhanced] Disclosure and Barring Services (DBS/EDBS)'),
		('None', 'None'),
	)
	sc = models.CharField(max_length=8, choices=SECURITY_CLEARANCE_CHOICES, default='None')

class Candidate(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField(max_length=128)
	phone = models.CharField(max_length=16)
	DV = models.BooleanField()
	SC = models.BooleanField()
	BPSS = models.BooleanField()
	CTC = models.BooleanField()
	NATO = models.BooleanField()
	MPS = models.BooleanField()
	SIA = models.BooleanField()
	DBS = models.BooleanField()

def upload_location(instance, filename):
	return "%s/%s" %(instance.customer, filename)

def validate_file_extension(value):
  import os
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.doc','.docx']
  if not ext in valid_extensions:
    raise ValidationError(u'File not supported!')


class AppRequest(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField(max_length=128)
	phone = models.CharField(max_length=16, blank=True, null=True)
	vendor = models.CharField(max_length=64)
	app = models.CharField(max_length=64)
	version = models.CharField(max_length=16)
	OS_CHOICES = (
		('Win10', 'Windows 10'),
		('Win81', 'Windows 8.1'),
		('Win7', 'Windows 7'),
		('WinXP', 'Windows XP'),
	)
	os = models.CharField(max_length=16, choices=OS_CHOICES, default='Win10')
	PACKAGE_TYPE_CHOICES = (
		('MSI', 'MSI'),
		('AppV46', 'App-V 4.6'),
		('AppV50', 'App-V 5.0'),
	)
	package_type = models.CharField(max_length=16, choices=PACKAGE_TYPE_CHOICES, default='MSI')
	COMPLEXITY_CHOICES = (
		('Simple', 'Simple'),
		('Medium', 'Medium'),
		('Complex', 'Complex'),
	)
	complexity = models.CharField(max_length=8, choices=COMPLEXITY_CHOICES, default='Medium')
	PRIORITY_CHOICES = (
		('High', 'High'),
		('Medium', 'Medium'),
		('Low', 'Low'),
	)
	priority = models.CharField(max_length=8, choices=PRIORITY_CHOICES, default='Low')
	comments = models.TextField(default='', blank=True, null=True)
	STATUS_CHOICES = (
		('Submitted', 'Submitted'),
		('Cancelled', 'Cancelled'),
		('Packaging', 'Packaging'),
		('UAT', 'UAT'),
		('Completed', 'Completed'),
	)
	status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='Submitted')
	date = models.DateField(auto_now_add=True)
	customer = models.CharField(max_length=32)
	assigned = models.CharField(max_length=64, default='Not Assigned')
	attachment = models.FileField(upload_to=upload_location, null=True, blank=True, validators=[validate_file_extension])
	reference = models.CharField(max_length=32)


	def get_absolute_url(self):
		return reverse('apprequest_detail', kwargs={'pk': self.pk})