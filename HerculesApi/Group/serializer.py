from django.contrib.auth.models import Group
from rest_framework import serializers

# from HerculesApi.Group.model import StoreAdminGroup


# class StoreAdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StoreAdminGroup
#         fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
