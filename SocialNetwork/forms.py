from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import *

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2")

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user