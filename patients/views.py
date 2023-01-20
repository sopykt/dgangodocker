from django.shortcuts import render
from .models import Patient
from .forms import Patient_form

# Create your views here.
def patient_create_view(request):
    form = Patient_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Patient_form()
    context = {
        'form': form
    }
    return render(request, 'patient_create.html', context)

def patient_detail_view(request):
    patient = Patient.objects.get(id=1)
    context = {
        'patient': patient
    }
    return render(request, 'patients.html', context)
