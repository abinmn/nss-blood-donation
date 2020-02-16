from rest_framework import viewsets
from app import models
from app import serializers


class DistrictViewset(viewsets.ReadOnlyModelViewSet):
    """Retrieve list of all districts."""

    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
