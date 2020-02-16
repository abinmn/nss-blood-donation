from rest_framework import serializers
from app import models


class DistrictSerializer(serializers.ModelSerializer):
    """Serialize district object."""
    class Meta:
        model = models.District
        fields = ('id', 'name')


class BloodGroupSerializer(serializers.ModelSerializer):
    """Serialize blood_group object."""
    class Meta:
        model = models.BloodGroup
        fields = ('id', 'group')
