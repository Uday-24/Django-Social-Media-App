from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            
    form = LoginForm()
    return render(request, 'users/login.html', {'form' : form})

@login_required
def index(request):
    return render(request, 'users/index.html')

def logout_page(request):
    logout(request)
    return redirect('login')