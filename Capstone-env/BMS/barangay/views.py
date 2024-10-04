from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages



from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
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