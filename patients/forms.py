from django.forms import ModelForm
from .models import Patient

class Patient_form(ModelForm):
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