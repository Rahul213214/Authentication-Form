
# from django.http import HttpResponseRedirect
import imp
from django.shortcuts import redirect, render,HttpResponseRedirect

#authentication
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required


# flash message
from django.contrib import messages

# Create your views here.

#Home Page View

def Home(request):
    return render(request, 'home.html')


#Authentication for farmer
#signup form farmer
def signupFarmer(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            user=fm.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            
            return redirect('login')

    else:
        fm=SignUpForm()
    return render(request,'signupfarmer.html',{'form':fm})

#login form farmer
def loginFarmer(request):
    if request.method=="POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/crud/')
            else:
                messages.info(request, "Username Or password is incorrect. ")
                # return render(request, 'login.html')
    else:
        fm=AuthenticationForm()

    fm=AuthenticationForm()
    return render(request, 'loginfarmer.html', {'form':fm})


#logout


def logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def crud_farmer(request):
    return render(request,'crudfarmer.html')
