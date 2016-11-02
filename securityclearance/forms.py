from django import forms
from django.forms import ModelForm

from .models import AppRequest
from .models import Candidate


class CandidateForm(ModelForm):
	class Meta:
		model = Candidate
		fields = '__all__'


class AppRequestForm(ModelForm):
	class Meta:
		model = AppRequest
		fields = ['vendor', 'app', 'version', 'os', 'package_type', 'complexity', 'priority', 'status', 'assigned', 'attachment', 'comments']

