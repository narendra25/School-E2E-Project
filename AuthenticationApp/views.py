from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from AuthenticationApp.models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.
#Login vIew Functionality 
#Login Validations

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def Login_View(request):
    if request.method=="POST":
        UserName=request.POST.get("username")
        Password=request.POST.get("password")
       
        myuser=authenticate(username=UserName,password=Password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Success')
            return redirect('/home')
        else:
            messages.error(request,'Invalid Credentials..')
            return redirect('/')

    return render(request,'Login.html')

#SignUp View  vIew Functionality 
#Sign Up Validations
def SignUp_View(request):
    if request.method=="POST":
        UserName=request.POST.get("username")
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        ConfirmPassword=request.POST.get("confirmpassword")
        #print(UserName,Email,Password,ConfirmPassword)
        if Password != ConfirmPassword:
           messages.warning(request,'Password is incorrect')
           return redirect('/signup')
        try:
            if User.objects.get(username=UserName):
                messages.warning(request,'UserName is Already Taken')
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=Email):
                messages.warning(request,'Email is Already Taken')
                return redirect('/signup')
        except:
            pass

        myuser=User.objects.create_user(UserName,Email,Password)
        myuser.save()
        messages.success(request,'Suceessfully completed your registration..Please Login!')
        return redirect('/')
    return render(request,'SignUp.html')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def LogOut(request):
    return render(request,'Base.html')