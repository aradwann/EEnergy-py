from django.contrib.gis import admin
from .models import EnergyResource


admin.site.register(EnergyResource, admin.GeoModelAdmin)

