# Generated by Django 3.0.5 on 2020-04-10 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('energy_resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='energyresource',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='energy_resources', to=settings.AUTH_USER_MODEL),
        ),
    ]