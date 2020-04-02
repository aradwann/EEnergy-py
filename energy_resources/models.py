from django.db import models
from django.conf import settings


class EnergyResource(models.Model):
    resource_type = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    capacity = models.FloatField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
