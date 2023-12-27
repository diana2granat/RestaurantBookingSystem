from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

class UserCreationForm (UserCreationForm):
    email = forms.EmailField(
        max_length=255,
        help_text="Your e-mail address is required",
        widget=forms.EmailInput(attrs={
            "class":"shadow appearence-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
            "placeholder":"Email"
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"shadow appearence-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
            "placeholder":"Password"
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"shadow appearence-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
            "placeholder":"Confirm Password"
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        self.fields['email'].required = True

class UserChangeForm (UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email',)
