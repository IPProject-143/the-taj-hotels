from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class ucform(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class DateInput(forms.DateInput):
    input_type = "date"

class dates(forms.Form):
    checkin = forms.DateField(widget = DateInput)
    checkout = forms.DateField(widget = DateInput)