from django.urls import path, re_path
from .import views
from django.views.generic import TemplateView
from django.urls import path, include  # new

urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='blog/index.html')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^register$', views.register, name='register'),
    re_path(r'^user$', views.userdashboard, name='userdashboard'),
    re_path(r'^login$', views.login, name='login'),
    re_path('accounts/logout/', views.logout, name='logout'),
    re_path(r'^admindashboard/$', views.admindashboard, name='admindashboard'),
    re_path(r'^admin/accounts/$', views.adminAccounts, name='adminAccounts'),
    re_path(r'^admin/service/$', views.adminService, name='adminService'),
    re_path(r'^admin/certificates/$', views.adminCertificates, name='adminCertificates'),
    re_path(r'^admin/event/$', views.adminEvent, name='adminEvent'),
    re_path(r'^admin/payment/$', views.adminPayment, name='adminPayment'),
    re_path(r'^admin/resident/$', views.adminResident, name='adminResident'),


    


















     #----------------------------------------Erwin------------------------------------------------




]

