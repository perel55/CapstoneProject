from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
  template = loader.get_template('accounts/login.html')
  return HttpResponse(template.render())


def signup(request):
  template = loader.get_template('accounts/signup.html')
  return HttpResponse(template.render())

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )

        # Authenticate and log in the user
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            auth_login(request, user)
            return redirect('userdashboard')  

    return render(request, 'master.html')

def userdashboard(request):
  template = loader.get_template('blog/userd.html')
  return HttpResponse(template.render())



@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log in the user
            auth_login(request, user)
            return redirect('userdashboard')  
        else:
            # Invalid credentials
            messages.error(request, "Invalid username or password.")
    
    # Render the login page
    return render(request, 'master.html')  


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
    


























































































#------------------------  SERVICES --------------------------#

def service_list(request):
    services = Services.objects.all()
    return render(request, 'ServiceList.html', {'services': services})

def AddService(request):
    if request.method == "POST":
        service_name = request.POST.get('service_name')
        requirements = request.POST.get('requirements')
        service_description = request.POST.get('service_description')
        service_price = request.POST.get('service_price')

        image = request.FILES.get('image')

        new_service = Services(
            service_name=service_name,
            requirements=requirements,
            service_description=service_description,
            service_price=service_price,
            image=image,
        )
        new_service.save()

        return redirect('service_list')

    return render(request, 'AddServices.html')

def update_service(request, service_id):
    service = get_object_or_404(Services, service_id=service_id)

    if request.method == "POST":
        service.service_name = request.POST.get('service_name')
        service.requirements = request.POST.get('requirements')
        service.service_description = request.POST.get('service_description')
        service.service_price = request.POST.get('service_price')

        if request.FILES.get('image'):
            service.image = request.FILES['image']

        service.save()
        return redirect('service_list')

    return render(request, 'update_service.html', {'service': service})


def delete_service(request, service_id):
    service = get_object_or_404(Services, service_id=service_id)
    service.delete()
    return redirect('service_list')

def administrative_services_list(request):
    services = Services.objects.all()
    return render(request, 'administrative_services_list.html', {'services': services})

def health_services_list(request):
    health_services = HealthService.objects.all()
    return render(request, 'health_services_list.html', {'health_services': health_services})

