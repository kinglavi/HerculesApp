from HerculesApi.Store.model import Store
from HerculesApi.Store.serializer import StoreSerializer
from rest_framework import viewsets


class StoreView(viewsets.ModelViewSet):
    serializer_class = StoreSerializer()
    queryset = Store.objects.all()