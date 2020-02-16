from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


from app import models
from app import serializers


class DistrictViewset(viewsets.ReadOnlyModelViewSet):
    """Retrieve list of all districts."""

    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer

    @swagger_auto_schema(responses={'200': serializers.DistrictDetailsSerializer})
    def retrieve(self, request, *args, **kwargs):
        """Change serializer to include Taluk data"""
        district = self.get_object()
        serializer = serializers.DistrictDetailsSerializer(district)  
        return Response(serializer.data)