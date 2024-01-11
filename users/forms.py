from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Student
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Student 
        fields = ['username', 'email', 'password1', 'password2']