from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'gender' ,'age' ,'experience_year', 'title' , 'location', 'avatar']
