from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.exceptions import PermissionDenied
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Job
from .models import Candidate
from .models import AppRequest
from .forms import AppRequestForm
from .forms import CandidateForm

import string

import csv
import xlwt
from export_xls.views import export_xlwt

from django.template import loader, Context

from django.core.mail import send_mail

def email(request):
	send_mail(
		'Subject here',
		'Here is the message.',
		'from@example.com',
		['to@example.com'],
		fail_silently=False,
	)


def splitcustomer(value, arg):
	a, b = value.split(arg)
	return a

def excel(request):
	group = request.user.groups.values_list('name',flat=True)[0]
	customer = splitcustomer(group, '-')
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="apprequests.xls"'
	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('AppRequests')
	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/mm/yyyy'
	# Sheet header, first row
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	columns = ['Reference', 'Vendor', 'App', 'Version', 'Package Type', 'Date', 'Priority', 'Status', 'Requestor', 'Assigned', 'Attachment' ]
	for col_num in xrange(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()
	rows = AppRequest.objects.filter(customer=customer).values_list('reference', 'vendor', 'app', 'version', 'package_type', 'date', 'priority', 'status', 'name', 'assigned', 'attachment')
	for row in rows:
		row_num += 1
		for col_num in xrange(len(row)):
			ws.write(row_num, col_num, row[col_num], date_format)
	wb.save(response)
	return response


class LoggedInMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)


def index(request):
	if request.user.is_authenticated():
		group = request.user.groups.values_list('name',flat=True)[0]
		customer = splitcustomer(group, '-')
	else:
		group = ''
		customer = ''
	apprequest = AppRequest.objects.filter(customer=customer).last
	return render(request, 'securityclearance/index.html', {
		'apprequest': apprequest,
	})

class AppRequestList(LoggedInMixin, ListView):
	model = AppRequest
	template_name = 'apprequest_list.html'
	def get_queryset(self):
		return AppRequest.objects.all()
	def get_context_data(self, **kwargs):
		group = self.request.user.groups.values_list('name',flat=True)[0]
		customer = splitcustomer(group, '-')
		context = super(AppRequestList, self).get_context_data(**kwargs)
		#context['apprequests'] = AppRequest.objects.filter(email=self.request.user)
		context['apprequests'] = AppRequest.objects.all()
		context['apprequest'] = AppRequest.objects.filter(customer=customer).last
		return context

class MyAppRequestList(LoggedInMixin, ListView):
	model = AppRequest
	template_name = 'apprequest_list.html'
	def get_queryset(self):
		return AppRequest.objects.all()
	def get_context_data(self, **kwargs):
		context = super(MyAppRequestList, self).get_context_data(**kwargs)
		context['apprequests'] = AppRequest.objects.filter(email=self.request.user)
		return context

class AssignedAppRequestList(LoggedInMixin, ListView):
	model = AppRequest
	template_name = 'apprequest_list.html'
	def get_queryset(self):
		return AppRequest.objects.all()
	def get_context_data(self, **kwargs):
		context = super(AssignedAppRequestList, self).get_context_data(**kwargs)
		context['apprequests'] = AppRequest.objects.filter(assigned=self.request.user)
		return context

class AppRequestDetail(LoggedInMixin, DetailView):
	model = AppRequest
	template_name = 'securityclearance/apprequest_detail.html'
	def get_context_data(self, **kwargs):
		context = super(AppRequestDetail, self).get_context_data(**kwargs)
		try:
			#context['apprequest'] = AppRequest.objects.get(id=self.kwargs['pk'], email=self.request.user)
			context['apprequest'] = AppRequest.objects.get(id=self.kwargs['pk'])
			return context
		except AppRequest.DoesNotExist:
			raise Exception('You are not authorised to view this request')

class AppRequestUpdate(LoggedInMixin, UpdateView):
	model = AppRequest
	template_name = 'securityclearance/apprequest_update.html'
	fields = ['vendor', 'app', 'version', 'os', 'package_type', 'complexity', 'priority', 'status', 'assigned', 'attachment', 'comments']
	def get_context_data(self, **kwargs):
		group = self.request.user.groups.values_list('name',flat=True)[0]
		customer = splitcustomer(group, '-')
		context = super(AppRequestUpdate, self).get_context_data(**kwargs)
		#context['apprequests'] = AppRequest.objects.filter(email=self.request.user)
		context['apprequests'] = AppRequest.objects.all()
		context['apprequest'] = AppRequest.objects.filter(customer=customer).last
		return context
	def get_initial(self):
		initial = super(UpdateView, self).get_initial()
		for k, v in self.request.GET.iterlists():
			if len(v)>1:
				initial.update({k:v})
			else:
				initial.update({k:v[0]})
		return initial

def apprequest_assign(request, id):
	try:
		apprequest = AppRequest.objects.get(id=id)
		assignees = AppRequest.objects.filter(customer=apprequest.customer).values('email').distinct()
		#assignees = AppRequest.objects.values('email').distinct()
	except AppRequest.DoesNotExist:
		raise Http404('This application request does not exist.')
	return render(request, 'securityclearance/apprequest_assign.html', {
		'apprequest': apprequest,
		'assignees': assignees,
	})

class AppRequestDelete(LoggedInMixin, DeleteView):
	model = AppRequest
	success_url = reverse_lazy('apprequests')

class AppRequestCreate(LoggedInMixin, CreateView):
 	model = AppRequest
	template_name = 'securityclearance/apprequest_form.html'
	fields = ['reference', 'comments', 'customer', 'name', 'email', 'phone', 'vendor', 'app', 'version', 'os', 'package_type', 'complexity', 'priority', 'status', 'assigned', 'attachment']
	def get_initial(self):
		initial = super(CreateView, self).get_initial()
		for k, v in self.request.GET.iterlists():
			if len(v)>1:
				initial.update({k:v})
			else:
				initial.update({k:v[0]})
		return initial


def summary(request):
	group = request.user.groups.values_list('name',flat=True)[0]
	if request.user.groups.filter(name=group).count():
		customer = string.replace(group, '-admin', '')
		customer = string.replace(customer, '-write', '')
		customer = string.replace(customer, '-read', '')
	else:
		customer = ''
	if customer == 'Global':
		apprequests = AppRequest.objects.all()
		packaging = AppRequest.objects.filter(status='Packaging')
		uat = AppRequest.objects.filter(status='UAT')
		cancelled = AppRequest.objects.filter(status='Cancelled')
		submitted = AppRequest.objects.filter(status='Submitted')
		completed = AppRequest.objects.filter(status='Completed')
	else:
		apprequests = AppRequest.objects.filter(customer=customer)
		packaging = AppRequest.objects.filter(status='Packaging', customer=customer)
		uat = AppRequest.objects.filter(status='UAT', customer=customer)
		cancelled = AppRequest.objects.filter(status='Cancelled', customer=customer)
		submitted = AppRequest.objects.filter(status='Submitted', customer=customer)
		completed = AppRequest.objects.filter(status='Completed', customer=customer)
	return render(request, 'securityclearance/summary.html', { 
		'apprequests': apprequests,
		'packaging': packaging,
		'uat': uat,
		'cancelled': cancelled,
		'submitted': submitted,
		'completed': completed,
	})

def docs(request):
	apprequests = AppRequest.objects.all()
	return render(request, 'securityclearance/docs.html', { 
		'apprequests': apprequests,
	})

def jobs(request):
	jobs = Job.objects.exclude(salary=0)
	return render(request, 'securityclearance/jobs.html', { 
		'jobs': jobs,
	})

def job_detail(request, id):
	try:
		job = Job.objects.get(id=id)
		my_keyword = job.sc
		my_filter = {}
		my_filter[my_keyword] = 'true'
		try:
			candidates = Candidate.objects.filter(**my_filter)
		except Candidate.DoesNotExist:
			name = 'Suitable candidate could not be found'		
	except Job.DoesNotExist:
		raise Http404('This job does not exist')
	return render(request, 'securityclearance/job_detail.html', {
		'job': job,
		'candidates': candidates,
	})

def candidates(request):
	candidates = Candidate.objects.exclude()
	return render(request, 'securityclearance/candidates.html', {
		'candidates': candidates,
	})
	
def candidate_detail(request, id):
	try:
		candidate = Candidate.objects.get(id=id)
	except Candidate.DoesNotExist:
		raise Http404('This candidate does not exist')
	return render(request, 'securityclearance/candidate_detail.html', {
		'candidate': candidate,
	})

def candidate_add(request):
	candidate = CandidateForm(request.POST or None)	
	if candidate.is_valid():
		save_it = candidate.save(commit=False)
		save_it.save()
		messages.success(request, 'Candidate added successfully.')
	return render_to_response('securityclearance/candidate_add.html', locals(), context_instance=RequestContext(request))

def candidate_delete(request, id):
	try:
		candidate = Candidate.objects.get(id=id)
		candidate.delete()
		candidates = Candidate.objects.all()
	except Candidate.DoesNotExist:
		raise Http404('This candidate does not exist.')
	return render(request, 'securityclearance/candidates.html', {
		'candidate': candidate,
		'candidates': candidates,
	})

