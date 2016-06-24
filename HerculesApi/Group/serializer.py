from rest_framework import serializers

from HerculesApi.Company.model import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('url', 'id', 'name')
