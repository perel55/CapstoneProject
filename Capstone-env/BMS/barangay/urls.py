from django.urls import path, re_path, include
from . import views
from django.views.generic import TemplateView
from django.urls import path, include  # new
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    re_path(r'^validatelogin/$', views.validatelogin, name='validatelogin'),
    re_path(r'^register$', views.register, name='register'),
    re_path(r'^residentDashboard/$', views.residentdashboard, name='residentdashboard'),
    re_path('accounts/logout/', views.logout, name='logout'),
    re_path(r'^admindashboard/$', views.admindashboard, name='admindashboard'),
    re_path(r'^admin/accounts/$', views.adminAccounts, name='adminAccounts'),
    re_path(r'^admin/service/$', views.adminService, name='adminService'),
    re_path(r'^admin/certificates/$', views.adminCertificates, name='adminCertificates'),
    re_path(r'^admin/event/$', views.adminEvent, name='adminEvent'),
    re_path(r'^admin/payment/$', views.adminPayment, name='adminPayment'),
    re_path(r'^admin/resident/$', views.adminResident, name='adminResident'),
    re_path(r'^admin/addAdmin/$', views.addAdmin, name='addAdmin'),
    re_path(r'^adminregister$', views.adminregister, name='adminregister'),








    #----------------------------------------Bhw------------------------------------------------
    re_path(r'^bhwDashboard/$', views.bhwDashboard, name='bhwDashboard'),
    re_path(r'^addBhw$', views.addBhw, name='addBhw'),
    re_path(r'^bhwregister/$', views.bhwregister, name='bhwregister'),
    re_path(r'^bhwService/$', views.bhwService, name='bhwService'),
    re_path(r'^bhwOutbreak/$', views.bhwOutbreak, name='bhwOutbreak'),
    re_path(r'^bhwRecord/$', views.bhwRecord, name='bhwRecord'),
    re_path(r'^bhwMedic/$', views.bhwMedic, name='bhwMedic'),
    re_path('bhw/addservice/', views.addHealthservice, name = 'addHealthservice'),
    re_path('bhwResidentlist/', views.bhwResidentlist, name = 'bhwResidentlist'),
    re_path('bhwEvents/', views.bhwEvents, name = 'bhwEvents'),
    re_path('bhwList/', views.bhwList, name = 'bhwList'),
    re_path(r'^resident/service/$', views.bhwServices, name='bhwServices'),
    re_path(r'^bhw/deleteService/(?P<HealthService_id>\d+)/$', views.delete_healthservice, name='delete_healthservice'),
    re_path(r'^bhw/UpdateService/(?P<HealthService_id>\d+)/$', views.update_healthservice, name='update_healthservice'),

    re_path(r'^bhw/book_healthServiceform/(?P<HealthService_id>\d+)/$', views.book_healthServiceform, name='book_healthServiceform'),
    re_path(r'^bhw/book_healthService/(?P<HealthService_id>\d+)/$', views.book_healthService, name='book_healthService'),
    
    
    
    


















     #----------------------------------------Erwin------------------------------------------------




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)