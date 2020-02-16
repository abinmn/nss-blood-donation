from rest_framework import serializers
from app import models


class BloodGroupSerializer(serializers.ModelSerializer):
    """Serialize blood_group object."""
    class Meta:
        model = models.BloodGroup
        fields = ('id', 'group')


class DistrictSerializer(serializers.ModelSerializer):
    """Serialize district object."""
    class Meta:
        model = models.District
        fields = ('id', 'name')


class TalukSerializer(serializers.ModelSerializer):
    """Serialize Taluk object."""
    class Meta:
        model = models.Taluk
        fields = ('id', 'name')


class DistrictDetailsSerializer(serializers.ModelSerializer):
    """Serialize district object."""

    taluks = TalukSerializer(many=True, read_only=True)

    class Meta:
        model = models.District
        fields = ('id', 'name', 'taluks')
