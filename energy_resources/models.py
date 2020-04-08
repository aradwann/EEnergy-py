from django.contrib.gis.db import models
from django.conf import settings


class EnergyResource(models.Model):
    resource_type = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    capacity = models.FloatField()
    location = models.PointField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='energy_resources', on_delete=models.CASCADE,)
