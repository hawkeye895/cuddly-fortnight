from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm,NewLoginForm,ProfilepicForm

# Create your views here.

def signin(request):
    if request.method=="POST":
        form= NewLoginForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as : {username}")
                return redirect("core:home")
            else:
                messages.error(request, f"Invalid Username or Password")
            
    form = NewLoginForm
    return render(request=request, 
                  template_name= "user/login_user.html", 
                  context={"form" :form})

def signout(request):
    logout(request)
    return redirect('core:visitor')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:home')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})
    
def get_user_profile(request):
    return render(request=request, template_name='user/user_profile.html')

def profile_picture(request):
    if request.method =='POST':
        form = ProfilepicForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form=ProfilepicForm()
    return render(request,'user/user_profile.html',{'form':form})
