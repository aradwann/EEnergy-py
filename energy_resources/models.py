from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class EnergyResource(models.Model):
    resource_type = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    capacity = models.FloatField()
    consumption = models.FloatField()
    location = models.PointField()
    net_energy = models.FloatField(default=0)

    owner = models.ForeignKey(
        get_user_model(), related_name='energy_resources', on_delete=models.CASCADE,)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.net_energy = self.capacity - self.consumption

        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return f'{self.owner.username}\'s {self.resource_type}'
