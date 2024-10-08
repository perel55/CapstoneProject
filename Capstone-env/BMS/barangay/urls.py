from django.urls import path, re_path
from .import views
from django.views.generic import TemplateView
from django.urls import path, include  # new
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    re_path(r'^validatelogin/$', views.validatelogin, name='validatelogin'),
    re_path(r'^register$', views.register, name='register'),
    re_path(r'^resident/dashboard$', views.residentdashboard, name='residentdashboard'),
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


    


















     #----------------------------------------Erwin------------------------------------------------

    re_path(r'^barangay_secretary_dashboard/$', views.barangay_secretary_dashboard, name='barangay_secretary_dashboard'),

    path('add_service/', views.add_service, name='add_service'),
    path('service_list/', views.service_list, name='service_list'),

    path('service/update/<int:service_id>/', views.update_service, name='update_service'),
    path('service/delete/<int:service_id>/', views.delete_service, name='delete_service'),

    path('residents/', views.residents_list, name='residents_list'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

