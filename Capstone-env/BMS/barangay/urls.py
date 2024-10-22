from django.urls import path, re_path, include
from . import views
from django.views.generic import TemplateView
from .views import CustomLogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='blog/index.html')),
    path('accounts/', include('allauth.urls')),
   
    re_path(r'^register$', views.register, name='register'),
    re_path(r'^user$', views.userdashboard, name='userdashboard'),
    re_path(r'^login$', views.login, name='login'),
    re_path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    
    # -------------------------- ERWIN ----------------------------- #
    path('AddService/', views.AddService, name='AddService'),
    path('service_list/', views.service_list, name='service_list'),
    path('service/update/<int:service_id>/', views.update_service, name='update_service'),
    path('service/delete/<int:service_id>/', views.delete_service, name='delete_service'),
    path('administrative-services/', views.administrative_services_list, name='administrative_services_list'),
    path('health-services/', views.health_services_list, name='health_services_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
