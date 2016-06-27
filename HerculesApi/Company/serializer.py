from HerculesApi.Group.serializer import GroupSerializer
from rest_framework import serializers

from HerculesApi.Company.model import Company


class CompanySerializer(serializers.ModelSerializer):
    managers = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('name', 'created_at', 'description', 'managers')
