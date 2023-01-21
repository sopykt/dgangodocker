from django.shortcuts import render
from .models import Patient
from .forms import Patient_form

# Create your views here.
def patient_create_model_view(request):
    form = Patient_form(request.POST or None)
    visitor = request.user
    if form.is_valid():
        form_status = str(visitor) + ' post Patient Form'
    else:
        form_status = str(visitor) + ' get Patient Form'
    print(form_status)
    if form.is_valid():
        form.save()
        form = Patient_form()
    context = {
        'form': form
    }
    return render(request, 'patient_create_model_form.html', context)

def patient_create_raw_view(request):
    print(request.GET)
    print(request.POST)
    print(request.POST.get('patient_name'))
    patient_name = request.POST.get('patient_name')
    date_of_birth = request.POST.get('date_of_birth')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    sex = request.POST.get('sex')
    if request.method == 'POST':
        Patient.objects.create(patient_name=patient_name,date_of_birth=date_of_birth,address=address,phone_number=phone_number,email=email,sex=sex)
    return render(request, 'patient_create_raw_form.html', {})

def patient_detail_view(request):
    patient = Patient.objects.get(id=1)
    context = {
        'patient': patient
    }
    return render(request, 'patients.html', context)
