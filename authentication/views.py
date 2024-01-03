from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from authentication.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import userInformation

def registration_view(request):
    context = {}
    if request.POST:
        print("submit!")
        form = RegistrationForm(
            {
                'first_name' : request.POST['first_name'],
                'last_name' : request.POST['last_name'],
                'username' : request.POST['username'],
                'email' : request.POST['email'],
                'password': request.POST['password'],
                'password1': request.POST['password'],
                'password2': request.POST['password']
            }
        )
        if form.is_valid():
            print("save!")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(request,username=username, password=raw_password)
            print(account)
            form.save()
            return redirect('event_list')
        else:
            context['registration_form'] = form
            return render(request, 'register.html', context)
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        return render(request, 'register.html', context)


def login_view(request):
    context = {}
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        print(form)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print(user)
            login(request,user)
            return redirect('event_list')
        else:
            context['login_form'] =form
            return render(request, 'login.html', context)
    else:
        form = AccountAuthenticationForm()
        context['login_form'] =form
        return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')
