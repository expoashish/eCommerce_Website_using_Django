from django import forms
from django.contrib.auth.models import User
from ecommerce.models import Vendor,Customer

class VendorForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','email','password']

class VendorAddForm(forms.ModelForm):
    class Meta():
        model=Vendor
        fields=['profile','address','phone_no']


class CustomerForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['first_name','email','password']

class CustomerAddForm(forms.ModelForm):
    class Meta():
        model=Customer
        fields=['profile','address','phone_no']