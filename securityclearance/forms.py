from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group

from .models import AppRequest
from .models import Candidate



class CandidateForm(ModelForm):
	class Meta:
		model = Candidate
		fields = '__all__'

class GroupForm(ModelForm):
	class Meta:
		model = Group
		fields = '__all__'

class AppRequestForm(ModelForm):
	class Meta:
		model = AppRequest
		fields = ['vendor', 'app', 'version', 'os', 'package_type', 'complexity', 'priority', 'status', 'assigned', 'attachment', 'comments']

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']