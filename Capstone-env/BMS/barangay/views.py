from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
  template = loader.get_template('accounts/login.html')
  return HttpResponse(template.render())


def signup(request):
  template = loader.get_template('accounts/signup.html')
  return HttpResponse(template.render())
