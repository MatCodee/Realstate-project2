# Generated by Django 3.2 on 2023-05-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_state', '0003_property_type_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='google_maps_url',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
