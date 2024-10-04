from django.urls import path, re_path
from .import views
from django.views.generic import TemplateView
from django.urls import path, include  # new
from .views import CustomLogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='blog/index.html')),
    path('accounts/', include('allauth.urls')),

    re_path(r'^register$', views.register, name='register'),
    re_path(r'^user$', views.userdashboard, name='userdashboard'),
    re_path(r'^login$', views.login, name='login'),
    re_path('logout/', CustomLogoutView.as_view(), name='logout'),
]

