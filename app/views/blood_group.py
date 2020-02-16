from rest_framework import viewsets
from app import models
from app import serializers


class BloodGroupViewset(viewsets.ReadOnlyModelViewSet):
    """Retrieve list of all blood groups."""

    queryset = models.BloodGroup.objects.all()
    serializer_class = serializers.BloodGroupSerializer