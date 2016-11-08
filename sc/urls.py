from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse, reverse_lazy

from securityclearance import views
from securityclearance.views import AppRequestList, AppRequestDetail, AppRequestUpdate, AppRequestDelete, AppRequestCreate, MyAppRequestList, AssignedAppRequestList, UserCreate, UserDetail, GroupCreate



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^myapprequests$', MyAppRequestList.as_view(), name='myapprequests'),
    url(r'^apprequests', AppRequestList.as_view(), name='apprequests'),
    url(r'^apprequests/assigned', AssignedAppRequestList.as_view(), name='apprequests_assigned'),
    url(r'^apprequest/(?P<id>\d+)/assign', views.apprequest_assign, name='apprequest_assign'),
    url(r'^apprequest/(?P<pk>\d+)/delete', AppRequestDelete.as_view(), name='apprequest_delete'),
    url(r'^apprequest/(?P<pk>\d+)/update', AppRequestUpdate.as_view(), name='apprequest_update'),
    url(r'^apprequest/(?P<pk>\d+)/', AppRequestDetail.as_view(), name='apprequest_detail'),
    url(r'^apprequest/create', AppRequestCreate.as_view(), name='apprequest_create'),
    url(r'^tracker$', views.jobs, name='tracker'),
    url(r'^summary$', views.summary, name='summary'),
    url(r'^excel$', views.excel, name='excel'),
    url(r'^docs$', views.docs, name='docs'),
    url(r'^jobs$', views.jobs, name='jobs'),
    url(r'^job/(?P<id>\d+)/', views.job_detail, name='job_detail'),
    url(r'^candidates$', views.candidates, name='candidates'),
    url(r'^candidate/(?P<id>\d+)/delete', views.candidate_delete, name='candidate_delete'),
    url(r'^candidate/(?P<id>\d+)/', views.candidate_detail, name='candidate_detail'), 
    url(r'^candidate/add', views.candidate_add, name='candidate_add'),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^user/(?P<pk>\d+)/', UserDetail.as_view(), name='user_detail'),
    url(r'^user/success', views.user_success, name='user_success'),
    url(r'^user/create', UserCreate.as_view(model=User, success_url='success'), name='user_create'),
    url(r'^group/success', views.group_success, name='group_success'),
    url(r'^group/create', GroupCreate.as_view(model=Group, success_url='success'), name='group_create'),
#    url(r'^user/create', UserCreate.as_view(model=User, success_url=reverse_lazy('user_detail')), name='user_create'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
