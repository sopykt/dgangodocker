from django import forms
from .models import Patient

class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'patient_name',
            'date_of_birth', 
            'address',
            'phone_number',
            'email',
            'sex'
        ]

class Django_pure_patient_form(forms.Form):
    patient_name = forms.CharField(max_length=255)
    date_of_birth = forms.DateField()
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    email = forms.EmailField()
    sex = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))