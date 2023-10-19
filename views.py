from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View  # Add this line to import View
from django.contrib.auth import login, authenticate ,logout
from django.http import HttpResponse
from .forms import CreateuserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# myapp/views.py
from .models import BusRoute
from .models import BusSchedule
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


def index(request):
    # Your view logic here
    return render(request, 'index.html')
def index_html(request):
    return render(request,'index.html')
def reg(request):
    return render(request,'registraion.html')
def about(request):
    # return HttpResponse("This is the about page")
    return render(request,'about_website.html')
@login_required(login_url='login_view')
def dashboard_view(request):
    # Your view logic goes here
    return render(request, 'dashboard.html')

def login_view(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard.html')#Here write the link for dashboard page 
        else:
            messages.info(request,'Username or password is incorrrect')
    
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login_view')

def register_view(request):
        form = CreateuserForm()
        if request.method =='POST':
            form = CreateuserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Account was created for "+ user)
                return redirect('login_view')
            
                
             
    
        
        context ={'form':form}
        return render(request, 'registration.html', context)
def bus_route_view(request):
    routes = BusRoute.objects.all()
    return render(request, 'timetable.html', {'routes': routes})

def timetable_view(request):
    schedules = BusSchedule.objects.all()
    return render(request, 'timetable.html', {'schedules': schedules})
# for restricting user dashboard page 
# @login_required(login_url='login_view')
# def dashboard(request):
#     return redirect()
# Create your views here.
