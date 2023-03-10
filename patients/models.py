from django.db import models
from django.urls import reverse

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), default='M')

    def __str__(self):
        return self.patient_name
    
    def get_absolute_url(self): 
        return reverse("patients:patient_detail_view", kwargs={"id": self.id})
    