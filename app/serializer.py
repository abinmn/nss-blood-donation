from rest_framework import serializers
from app import models


class DistrictSerializer(serializers.ModelSerializer):
    """Serialize district object."""
    class Meta:
        model = models.District
        fields = ('id', 'name')
