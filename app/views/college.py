from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


from app import models
from app import serializers


class CollegeByTalukViewset(viewsets.ViewSet):
    """Retrieve list of all colleges in a taluk."""

    def list(self, request):
        queryset = self.get_queryset()
        requested_blood_group = int(request.query_params.get('blood_group'))

        serializer = serializers.SearchByTalukSerializer(
            queryset, many=True, context={
                'requested_blood_group': requested_blood_group})

        return Response(serializer.data)

    def get_queryset(self):
        taluk_id = int(self.request.query_params.get('taluk'))
        blood_group_id = int(self.request.query_params.get('blood_group'))
        colleges = models.Taluk.objects.get(id=taluk_id).colleges.all()
        return colleges
