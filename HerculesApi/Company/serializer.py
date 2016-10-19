from django.contrib.auth.models import Group

from HerculesApi.Group.functions import create_group
from HerculesApi.Group.serializer import GroupSerializer
from rest_framework import serializers

from HerculesApi.Company.model import Company


class CompanySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        requested_user = self.context['request'].user
        if requested_user not in validated_data['managers']:
            validated_data['managers'].append(requested_user)
        return super(CompanySerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        requested_user = self.context['request'].user
        if requested_user not in validated_data['managers']:
            validated_data['managers'].append(requested_user)
        return super(CompanySerializer, self).update(validated_data)

    class Meta:
        model = Company
        fields = ('name', 'created_at', 'description', 'managers', 'id')
