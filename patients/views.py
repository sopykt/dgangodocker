from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Patient
from .forms import Patient_form, Django_pure_patient_form

# Create your views here.
def patients_list_view(request):
    all_patients = Patient.objects.all()
    context = {
        "all_patients": all_patients
    }
    return render(request, 'patients_list.html', context)

def patient_create_django_pure_view(request):
    # one way to add initial
    initial_data = {'date_of_birth': '1980-05-14'}
    form = Django_pure_patient_form(request.POST or None, initial=initial_data)
    visitor = request.user
    if form.is_valid():
        form_status = str(visitor) + ' post Patient Django Form'
    else:
        form_status = str(visitor) + ' get Patient Django Form'
    print(form_status)
    if form.is_valid():
        Patient.objects.create(**form.cleaned_data)
        form = Django_pure_patient_form()
    context = {
        "form": form
    }
    return render(request, 'patient_create_django_pure_form.html', context)


def patient_edit_model_view(request, id):
    # edit existing Patient object
    obj = Patient.objects.get(id=id)
    form = Patient_form(request.POST or None, instance=obj)
    visitor = request.user
    if form.is_valid():
        form_status = str(visitor) + ' post Patient Model Form'
    else:
        form_status = str(visitor) + ' get Patient Model Form'
    print(form_status)
    if form.is_valid():
        form.save()
        # form = Patient_form()
        return redirect('/patients/' + str(id))
    context = {
        'form': form
    }
    return render(request, 'patient_edit_model_form.html', context)

def patient_delete_view(request, id):
    
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        query_name = request.POST.get('patient_name')
        if query_name == patient.patient_name:
            patient.delete()
            return redirect('/patients')
    context = {
        'patient': patient
    }
    return render(request, 'patient_delete_view.html', context)

def patient_create_raw_view(request):
    patient_name = request.POST.get('patient_name')
    date_of_birth = request.POST.get('date_of_birth')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    sex = request.POST.get('sex')
    if request.method == 'POST':
        Patient.objects.create(patient_name=patient_name,date_of_birth=date_of_birth,\
            address=address,phone_number=phone_number,email=email,sex=sex)
    return render(request, 'patient_create_raw_form.html', {})

def patient_detail_view(request, id):
    # first way to handle does not exist
    # try:
    #     patient = Patient.objects.get(id=id)
    # except Patient.DoesNotExist:
    #     raise Http404
    
    # Better way to handle does not exist
    patient = get_object_or_404(Patient, id=id)
    context = {
        'patient': patient
    }
    return render(request, 'single_patient.html', context)
