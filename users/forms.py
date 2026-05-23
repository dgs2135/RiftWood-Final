from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address_line1 = forms.CharField(label="Address Line 1", max_length=255, required=True)
    address_line2 = forms.CharField(label="Address Line 2", max_length=255, required=False)
    zip_code = forms.CharField(label="Zip Code", max_length=20, required=False)
    city = forms.CharField(label="City", max_length=100, required=True)
    state = forms.CharField(label="State/Province", max_length=100, required=True)
    country = forms.CharField(label="Country", max_length=100, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'address_line1', 'address_line2', 'zip_code', 'city', 'state', 'country']

class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    address_line1 = forms.CharField(label="Address Line 1", max_length=255, required=True)
    address_line2 = forms.CharField(label="Address Line 2", max_length=255, required=False)
    zip_code = forms.CharField(label="Zip Code", max_length=20, required=False)
    city = forms.CharField(label="City", max_length=100, required=True)
    state = forms.CharField(label="State/Province", max_length=100, required=True)
    country = forms.CharField(label="Country", max_length=100, required=True)

    class Meta:
        model = Profile
        fields = [
            'address_line1', 'address_line2', 'zip_code', 'city', 'state', 'country'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email
            self.fields['username'].initial = self.instance.user.username
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['address_line1'].initial = self.instance.address_line1
            self.fields['address_line2'].initial = self.instance.address_line2
            self.fields['zip_code'].initial = self.instance.zip_code
            self.fields['city'].initial = self.instance.city
            self.fields['state'].initial = self.instance.state
            self.fields['country'].initial = self.instance.country

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
            
            user = profile.user
            user.email = self.cleaned_data.get('email', '')
            user.username = self.cleaned_data.get('username', '')
            user.first_name = self.cleaned_data.get('first_name', '')
            user.last_name = self.cleaned_data.get('last_name', '')
            user.save()
        return profile

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
