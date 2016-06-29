from rest_framework import viewsets

from HerculesApi.Group.model import StoreAdminGroup
from HerculesApi.Group.serializer import StoreAdminSerializer


class StoreAdminGroupsView(viewsets.ModelViewSet):
    serializer_class = StoreAdminSerializer
    queryset = StoreAdminGroup.objects.all()
