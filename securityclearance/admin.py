from django.contrib import admin

from .models import Job
from .models import Candidate
from .models import AppRequest

class JobAdmin(admin.ModelAdmin):
	list_display = ['title', 'salary', 'company', 'sc']

class CandidateAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'email', 'DV', 'SC', 'BPSS', 'CTC', 'NATO', 'MPS', 'SIA', 'DBS']

class AppRequestAdmin(admin.ModelAdmin):
	list_display = ['app', 'vendor', 'version', 'os', 'package_type', 'complexity', 'name', 'phone', 'email', 'customer']

admin.site.register(Job, JobAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(AppRequest, AppRequestAdmin)