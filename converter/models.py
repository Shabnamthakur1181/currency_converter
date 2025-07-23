# converter/models.py
from django.db import models

class ConversionHistory(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    amount = models.FloatField()
    result = models.FloatField()
    converted_at = models.DateTimeField(auto_now_add=True)
