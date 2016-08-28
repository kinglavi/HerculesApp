from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from HerculesApi.Store.model import Store
from HerculesApi.Store.serializer import StoreSerializer
from rest_framework import viewsets


class StoreView(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

@api_view(['GET'])
def store_view(request, store_id):
    return Response(get_gifts_by_store(request.user, int(store_id)), status=HTTP_200_OK)