from HerculesApi.Company.serializer import CompanySerializer
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'address', 'name',
                  'created_at', 'phone_number',
                  'company')
