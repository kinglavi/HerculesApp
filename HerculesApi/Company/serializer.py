from django.contrib.auth.models import Group

from HerculesApi.Group.functions import create_group
from HerculesApi.Group.serializer import GroupSerializer
from rest_framework import serializers

from HerculesApi.Company.model import Company


class CompanySerializer(serializers.ModelSerializer):
    managers = GroupSerializer(many=False, read_only=True)

    def create(self, validated_data):
        company_name = validated_data['name']
        g = create_group(self.context['request'].user, company_name)
        validated_data['managers'] = g
        return super(CompanySerializer, self).create(validated_data)

    class Meta:
        model = Company
        fields = ('name', 'created_at', 'description', 'managers')
