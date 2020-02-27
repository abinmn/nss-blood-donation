from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


from app.models import Student
from app.permissions import IsAllowedToModify
from app.serializers import StudentSerializer

@method_decorator
class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, IsAllowedToModify,)

    def get_queryset(self):
        user_college = self.request.user.volunteerprofile.college
        return Student.objects.filter(college=user_college)

    def create(self, request, *args, **kwargs):
        college = request.user.volunteerprofile.college
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(college=college)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
