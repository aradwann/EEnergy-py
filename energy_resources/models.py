from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class EnergyResource(models.Model):
    resource_type = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    capacity = models.FloatField()
    consumption = models.FloatField()
    location = models.PointField()

    owner = models.ForeignKey(
        get_user_model(), related_name='energy_resources', on_delete=models.CASCADE,)

    def net_energy(self):
        return self.capacity - self.consumption

    def __str__(self):
        return f'{self.owner.username}\'s {self.resource_type}'
