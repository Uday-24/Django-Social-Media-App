from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'shadow appearance-none border rounded-lg w-full py-2 pl-10 pr-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'shadow appearance-none border rounded-lg w-full py-2 pl-10 pr-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-indigo-500',
            'placeholder': 'Password'
        })
    )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'block w-full border border-gray-300 rounded-md py-2 pl-3 pr-10 focus:outline-none focus:ring focus:ring-indigo-500',
        'placeholder': 'Enter your password',
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'block w-full border border-gray-300 rounded-md py-2 pl-3 pr-10 focus:outline-none focus:ring focus:ring-indigo-500',
        'placeholder': 'Confirm your password',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full border border-gray-300 rounded-md py-2 pl-3 pr-10 focus:outline-none focus:ring focus:ring-indigo-500',
                'placeholder': 'Enter your username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full border border-gray-300 rounded-md py-2 pl-3 pr-10 focus:outline-none focus:ring focus:ring-indigo-500',
                'placeholder': 'Enter your email',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'block w-full border border-gray-300 rounded-md py-2 pl-3 pr-10 focus:outline-none focus:ring focus:ring-indigo-500',
                'placeholder': 'Enter your first name',
            }),
        }

    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data['password2']