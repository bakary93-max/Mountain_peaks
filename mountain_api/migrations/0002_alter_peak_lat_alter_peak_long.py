# Generated by Django 4.1.7 on 2023-02-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountain_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peak',
            name='lat',
            field=models.DecimalField(decimal_places=18, max_digits=25),
        ),
        migrations.AlterField(
            model_name='peak',
            name='long',
            field=models.DecimalField(decimal_places=18, max_digits=25),
        ),
    ]
