from rest_framework import serializers

from .models import Peak


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Peak
        fields = ['lat', 'long', 'name']
