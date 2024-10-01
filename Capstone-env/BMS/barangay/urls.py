from django.urls import path
from .import views
from django.views.generic import TemplateView
from django.urls import path, include  # new

urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='blog/index.html')),
    path('accounts/', include('allauth.urls')),
]

