from typing_extensions import Required
from django.db import models

# Create your models here.
class MoneyfiModel(models.Model):
    mf_name = models.CharField(max_length=200)
    mf_units = models.FloatField(max_length=10)
    mobile = models.CharField(max_length=10)
    class Meta:
        unique_together = ['mf_name', 'mf_units', 'mobile']
    def __str__(self):
        return self.mf_name

class MfCode(models.Model):
    mf_code = models.IntegerField()

    def __str__(self):
        return str(self.mf_code)

class MfDate(models.Model):
    mf_date = models.CharField(max_length=15)

    def __str__(self):
        return self.mf_date