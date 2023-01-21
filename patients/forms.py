from django import forms
from .models import Patient

class Patient_form(forms.ModelForm):
    # Not necessory but override model form field with django form field
    patient_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'special'}))
    date_of_birth = forms.DateField()
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    email = forms.EmailField()
    sex = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
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
        
    # Validate fields
    def clean_patient_name(self, *args, **kwargs):
        patient_name = self.cleaned_data.get('patient_name')
        if 'U ' in patient_name or 'Daw ' in patient_name:
            raise forms.ValidationError('Name should not include U or Daw')
        return patient_name

class Django_pure_patient_form(forms.Form):
    patient_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'special'}))
    date_of_birth = forms.DateField()
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    email = forms.EmailField()
    sex = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))