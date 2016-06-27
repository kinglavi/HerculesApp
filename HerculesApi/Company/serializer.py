from rest_framework import serializers

from HerculesApi.Company.model import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('url', 'id', 'name')
