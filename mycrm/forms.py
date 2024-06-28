from .models import Record
from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email  = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'EmailAddress'}))

    first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     super().__init__(*args, **kwargs)

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}), label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}), label='')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'email', 'class':'form-control'}), label='')
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'phone', 'class':'form-control'}), label='')
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'address', 'class':'form-control'}), label='')
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'city', 'class':'form-control'}), label='')
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'state', 'class':'form-control'}), label='')
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'zipcode', 'class':'form-control'}), label='')

    class Meta:
        model = Record
        exclude = ('user',)