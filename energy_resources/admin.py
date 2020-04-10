from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import EnergyResource


admin.site.register(EnergyResource, OSMGeoAdmin)
