from django.urls import path
from .views import (patients_list_view, patient_detail_view, patient_edit_model_view,
                    patient_delete_view, patient_create_raw_view, patient_create_django_pure_view)

app_name = 'patients'
urlpatterns = [
    path('', patients_list_view, name='patients_list_view'),
    path('<int:id>', patient_detail_view, name='patient_detail_view'),
    path('<int:id>/edit_patient_modelform', patient_edit_model_view, name='patient_edit_model_view'),
    path('<int:id>/delete_patient_view', patient_delete_view, name='patient_delete_view'),
    path('create_patient_rawform', patient_create_raw_view, name='patient_create_raw_view'),
    path('create_patient_django_pure_form', patient_create_django_pure_view, name='patient_create_django_pure_view'),
]
