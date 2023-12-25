from django.db import models

# Create your models here.
class State_region(models.Model):
    SR_PCODE = models.CharField(max_length=30)
    SR       = models.CharField(max_length=30)
    SR_MM3   = models.CharField(max_length=30)
    SA_PCODE = models.CharField(max_length=30)
    SA       = models.CharField(max_length=30)
    SA_MM3   = models.CharField(max_length=30)
    DT_PCODE = models.CharField(max_length=30)
    DT       = models.CharField(max_length=30)
    DT_MM3   = models.CharField(max_length=30)
    TS_PCODE = models.CharField(max_length=30)
    TS       = models.CharField(max_length=30)
    TS_MM3   = models.CharField(max_length=30)
    TN_PCODE = models.CharField(max_length=30)
    TN       = models.CharField(max_length=30)
    TN_MM3   = models.CharField(max_length=30)
    WD_PCODE = models.CharField(max_length=30)
    WD       = models.CharField(max_length=30)
    WD_MM3   = models.CharField(max_length=30)
    VT_PCODE = models.CharField(max_length=30)
    VT       = models.CharField(max_length=30)
    VT_WIN   = models.CharField(max_length=30)
    VT_MM3   = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.SR
    
class Special_admin(models.Model):
    State_region = models.ForeignKey(State_region,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.SA
    
class District(models.Model):
    
    def __str__(self) -> str:
        return self.DT
    
class Township(models.Model):
    
    def __str__(self) -> str:
        return self.TS
    
class Town(models.Model):
    
    def __str__(self) -> str:
        return self.TN
    
class Ward(models.Model):
    
    def __str__(self) -> str:
        return self.WD
    
class Village_tract(models.Model):
    
    def __str__(self) -> str:
        return self.VT
    
class Sub_township(models.Model):
    SUB_TS = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.SUB_TS