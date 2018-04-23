from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    """docstring for Userform"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    """docstring for UserProfileInfoForm"""
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio', 'profile_pic')
