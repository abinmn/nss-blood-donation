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
        blood_group = models.BloodGroup.objects.get(id=blood_group_id).group
        return blood_group


    def get_blood_group_count(self, college):
        count = college.blood_group_count(self.context.get('requested_blood_group'))
        return count
