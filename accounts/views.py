from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['inputPassword'] == request.POST['inputConfPass']:
            try:
                user = User.objects.get(username=request.POST['inputUsername'])
                return render(request, 'accounts/signup.html', {'error':"The username you entered has already been taken! Please try a different one."})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['inputUsername'], password=request.POST['inputPassword'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':"Passwords must match."})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['inputUsername'], password=request.POST['inputPassword'],)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:  
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')