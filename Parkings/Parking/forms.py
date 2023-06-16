from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ReservationParking


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReservationParkingForm(forms.ModelForm):
    destination = forms.CharField(max_length=100)  # Add the destination field
    date = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y'))
    time = forms.TimeField()

    class Meta:
        model = ReservationParking
        fields = ['destination', 'date', 'time']  # Add other fields as needed
