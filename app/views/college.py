from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter
from drf_yasg import openapi


from app import models
from app import serializers
from app.exceptions import QueryParameterRequiredException


class CollegeByTalukViewset(viewsets.ViewSet):
    """Retrieve list of all colleges in a taluk."""

    @swagger_auto_schema(responses={'200': serializers.SearchByTalukSerializer}, manual_parameters=[
                         Parameter(
                             name='blood_group',
                             required=True,
                             in_=openapi.IN_QUERY,
                             type=openapi.TYPE_INTEGER),
                         Parameter(
                             name='taluk',
                             required=True,
                             in_=openapi.IN_QUERY,
                             type=openapi.TYPE_INTEGER),
                         ])
    def list(self, request):
<<<<<<< HEAD
        queryset = self.get_queryset()
        requested_blood_group = self.request.query_params.get('blood_group')
=======
        queryset = self.get_queryset(blood_group_count)
        requested_blood_group = int(request.query_params.get('blood_group'))
>>>>>>> 2ccadf0ed9be836b61a2055e4589a40c8f6942aa

        serializer = serializers.SearchByTalukSerializer(
            queryset, many=True, context={
                'requested_blood_group': int(requested_blood_group)})

        return Response(serializer.data)

    def get_queryset(self):
        taluk_id = self.request.query_params.get('taluk', None)
        requested_blood_group = self.request.query_params.get(
            'blood_group', None)

        if taluk_id is None or requested_blood_group is None:
            raise QueryParameterRequiredException(['taluk_id', 'blood_group'])

        colleges = models.Taluk.objects.get(id=int(taluk_id)).colleges.all()
        return colleges


class CollegeDetailsViewset(viewsets.ReadOnlyModelViewSet):
    """Get contact details and other blood group details in a college."""
    queryset = models.College.objects.all()
<<<<<<< HEAD
    serializer_class = serializers.CollegeSerializer
=======
    serializer_class = serializers.CollegeSerializer
>>>>>>> 2ccadf0ed9be836b61a2055e4589a40c8f6942aa
