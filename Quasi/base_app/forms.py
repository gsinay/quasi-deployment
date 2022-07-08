
from django import forms
from django.contrib.auth.models import User
from base_app.models import UserProfileinfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']
    class Meta():
       model = User
       fields = ('username', 'email', 'password')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileinfo
        fields = ('date_of_birth', 'profile_pic')

