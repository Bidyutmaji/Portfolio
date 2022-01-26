from typing_extensions import Required
from django.db import models

# Create your models here.
class MoneyfiModel(models.Model):
    mf_name = models.CharField(max_length=200)
    mf_units = models.FloatField(max_length=10)
    mobile = models.IntegerField()
    class Meta:
        unique_together = ['mf_name', 'mf_units', 'mobile']
    def __str__(self):
        return self.mf_name