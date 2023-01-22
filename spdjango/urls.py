"""spdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, result_view
from patients.views import patient_detail_view, patient_edit_model_view, \
patient_create_raw_view, patient_create_django_pure_view, patient_delete_view, patients_list_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_view, name='home'),
    path('patients', patients_list_view, name='patients_list_view'),
    path('patient/<int:id>', patient_detail_view, name='patient_detail_view'),
    path('edit_patient_modelform/<int:id>', patient_edit_model_view, name='patient_edit_model_view'),
    path('delete_patient_view/<int:id>', patient_delete_view, name='patient_delete_view'),
    path('create_patient_rawform', patient_create_raw_view, name='patient_create_raw_view'),
    path('create_patient_django_pure_form', patient_create_django_pure_view, name='patient_create_django_pure_view'),
    path('result', result_view, name='result')
]
