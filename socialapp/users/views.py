from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from posts.models import Post
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

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    current_user = request.user
    posts = Post.objects.filter(user = current_user)
    return render(request, 'users/index.html', {'posts' : posts})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('register_done')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form':form})

def register_done(request):
    return render(request, 'users/register_done.html')


@login_required(login_url='login')
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print("Edit success")
        else:
            print("Edit failed")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'users/edit.html', {'user_form':user_form, 'profile_form':profile_form})