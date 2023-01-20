from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), default=None)

    def __str__(self):
        return self.patient_name