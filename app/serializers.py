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


class SearchByTalukSerializer(serializers.ModelSerializer):

    requested_blood_group = serializers.SerializerMethodField()
    blood_group_count = serializers.SerializerMethodField()

    class Meta:
        model = models.College
        fields = (
            'id',
            'name',
            'location',
            'requested_blood_group',
            'blood_group_count',
        )

    def get_requested_blood_group(self, college):
        blood_group_id = self.context.get('requested_blood_group')
        if blood_group_id:
            return models.BloodGroup.objects.get(id=blood_group_id).group
        return None

    def get_blood_group_count(self, college):
        blood_group = self.context.get('requested_blood_group')
        if blood_group:
            return college.blood_group_count_by_id(blood_group)
        return None


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VolunteerProfile
        depth = 1
        fields = (
            'name',
            'email',
            'mobile_number'
        )


class CollegeSerializer(serializers.ModelSerializer):

    blood_group_count = serializers.SerializerMethodField()
    poc_details = serializers.SerializerMethodField()

    class Meta:
        model = models.College
        fields = (
            'id',
            'name',
            'location',
            'blood_group_count',
            'poc_details'
        )

    def get_blood_group_count(self, college):
        return college.blood_group_count()

    def get_poc_details(self, college):
        volunteers = college.volunteer_details()
        return volunteers


class StudentSerializer(serializers.ModelSerializer):

    # blood_group_id = serializers.PrimaryKeyRelatedField(queryset=models.BloodGroup.objects.all())
    # blood_group = serializers.CharField(source='blood_group.group')

    blood_group = BloodGroupSerializer(read_only=True)
    blood_group_id = serializers.PrimaryKeyRelatedField(
        queryset=models.BloodGroup.objects.all(), write_only=True, source='blood_group')

    class Meta:
        model = models.Student
        fields = (
            'id',
            'name',
            'department',
            'phone_number',
            'email',
            'passout_year',
            'height',
            'weight',
            'gender',
            'blood_group',
            'blood_group_id',
        )

    def get_blood_group(self, student):
        return student.blood_group.name
