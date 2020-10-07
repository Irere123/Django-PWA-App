from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def profile(request):
    return render(request, 'users/profile.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method ==  'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' +  user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'users/register.html', context)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username , password= password)

        if user is not None:
            login(request, user)
            return redirect('journal:index')
        else:
            messages.warning(request, 'Username OR Password is incorrect ')


    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('journal:index')
