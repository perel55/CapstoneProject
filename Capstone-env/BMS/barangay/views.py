from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import Residents, Account_Type, Accounts
from django.contrib.auth import logout
from django.views import View
from .models import *
# Create your views here.

#Register Residents
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password1,
            )

            resident = Residents.objects.create(
                auth_user=user,
            )

            resident_account_type = Account_Type.objects.get(Account_type='Resident')

            newAcc = Accounts.objects.create(
                resident_id=resident,
                account_typeid=resident_account_type
            )


            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)  
                return redirect('residentdashboard')
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'account/signup.html')

#Register Admin
@csrf_exempt
def adminregister(request):
    # Retrieve account types for the dropdown
    account_types = Account_Type.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        account_type_id = request.POST.get('account_type')  # Get the selected account type

        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
            )

            # Create a resident record
            resident = Residents.objects.create(
                auth_user=user,
            )

            # Retrieve the selected account type based on the ID
            try:
                resident_account_type = Account_Type.objects.get(id=account_type_id)
            except Account_Type.DoesNotExist:
                messages.error(request, "Invalid account type selected.")
                return render(request, 'admin/addAdmin.html', {'account_types': account_types})

            # Create an account with the specified account type
            Accounts.objects.create(
                resident_id=resident,
                account_typeid=resident_account_type
            )

            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)  
                return redirect('admindashboard')
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'admin/addAdmin.html', {'account_types': account_types})

#login
@csrf_exempt
def validatelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            try:
                profile = Accounts.objects.get(resident_id__auth_user=user)
                account_type = profile.account_typeid.Account_type

                if account_type == 'Resident':
                    return redirect('residentdashboard')
                elif account_type == 'Admin':
                    return redirect('admindashboard')
                elif account_type == 'barangay_secretary':
                    return redirect('barangay_secretary_dashboard')
                else:
                    return redirect('defaultdashboard')

            except Accounts.DoesNotExist:
                messages.error(request, "User profile not found.")
                return redirect('login')

        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'account/login.html')


def index(request):
    return render(request, 'index.html')

def signup(request):
  template = loader.get_template('accounts/signup.html')
  return HttpResponse(template.render())

def residentdashboard(request):
    return render(request, 'resident/userd.html')



def admindashboard(request):
    return render(request, 'admin/admin.html')

def adminAccounts(request):
    return render(request, 'admin/adminAccounts.html')

def adminService(request):
    return render(request, 'admin/adminService.html')

def adminCertificates(request):
    return render(request, 'admin/adminCertificates.html')

def adminEvent(request):
    return render(request, 'admin/adminEvent.html')

def adminPayment(request):
    return render(request, 'admin/adminPayment.html')

def adminResident(request):
    return render(request, 'admin/adminResident.html')

def addAdmin(request):
    return render(request, 'admin/addAdmin.html')







































# --------------------------------- Erwin Views -------------------------------- #

def barangay_secretary_dashboard(request):
    services = Services.objects.all()
    return render(request, 'barangay_secretary/service_list.html', {'services': services})


def service_list(request):
    services = Services.objects.all()
    return render(request, 'barangay_secretary/service_list.html', {'services': services})

def add_service(request):
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

    return render(request, 'barangay_secretary/add_service.html')

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

    return render(request, 'barangay_secretary/update_service.html', {'service': service})


def delete_service(request, service_id):
    service = get_object_or_404(Services, service_id=service_id)
    service.delete()
    return redirect('service_list')

def residents_list(request):
    residents = Residents.objects.all()
    return render(request, 'barangay_secretary/barangay_resident.html', {'residents': residents}) 

