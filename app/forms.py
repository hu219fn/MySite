from django.contrib.auth import forms as formsAuth
from django.contrib.auth.models import User
from django import forms
from .models import *

class SignupForm(formsAuth.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'description']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description','file', 'url']