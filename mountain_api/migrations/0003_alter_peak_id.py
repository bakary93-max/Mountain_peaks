# Generated by Django 4.1.7 on 2023-02-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountain_api', '0002_alter_peak_lat_alter_peak_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peak',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
