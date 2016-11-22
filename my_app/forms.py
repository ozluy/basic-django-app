from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'gender' ,'age' ,'experience_year', 'title' , 'location', 'image']

class LoginForm(forms.Form):
    username = forms.CharField(label = 'User Name', max_length = 64, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'form-control'}))
