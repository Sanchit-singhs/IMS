from django import forms

from .models import User_s

class PostForm(forms.ModelForm):

    class Meta:
        model = User_s
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')