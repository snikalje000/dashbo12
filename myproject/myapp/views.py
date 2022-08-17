from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
   return render(request,'dash.html')

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )
            return redirect('/login')
        
    context={'form':form}
    return render(request,'register.html',context)


def loginPage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            messages.info(request,'Username OR Password is incorrect')
           
        
    context={}
    return render(request,'login.html',context)


def logout(request):
    logout(request)
    return redirect('login')



def landing(request):
    return render(request,'landing.html')


@login_required(login_url='/login/')
def dashboard(request):
    return render(request,'dashboard.html')


def dash1(request):
    return render(request,'dashboard/dash1.html')
def dash2(request):
    return render(request,'dashboard/dash2.html')
def dash3(request):
    return render(request,'dashboard/dash3.html')
def dash4(request):
    return render(request,'dashboard/dash4.html')
def dash5(request):
    return render(request,'dashboard/dash5.html')
def dash6(request):
    return render(request,'dashboard/dash6.html')
def dash7(request):
    return render(request,'dashboard/dash7.html')
def dash8(request):
    return render(request,'dashboard/dash8.html')
def dash9(request):
    return render(request,'dashboard/dash9.html')
def dash10(request):
    return render(request,'dashboard/dash10.html')
def dash11(request):
    return render(request,'dashboard/dash11.html')
def dash12(request):
    return render(request,'dashboard/dash12.html')
def dash13(request):
    return render(request,'dashboard/dash13.html')
def dash14(request):
    return render(request,'dashboard/dash14.html')
def dash15(request):
    return render(request,'dashboard/dash15.html')
def dash16(request):
    return render(request,'dashboard/dash16.html')
def dash17(request):
    return render(request,'dashboard/dash17.html')
def dash18(request):
    return render(request,'dashboard/dash18.html')
def dash19(request):
    return render(request,'dashboard/dash19.html')
def dash20(request):
    return render(request,'dashboard/dash20.html')
def dash21(request):
    return render(request,'dashboard/dash21.html')

