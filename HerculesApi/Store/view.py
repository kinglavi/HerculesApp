from HerculesApi.Permissions.permissions import is_admin_or_company_manager
from HerculesApi.Store.functions import get_gifts_by_store
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from HerculesApi.Store.model import Store
from HerculesApi.Store.serializer import StoreSerializer
from rest_framework import viewsets


class StoreView(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, company_id=request.data['company']):
            return super(StoreView, self).create(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can create stores.")

    def update(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, company_id=request.data['company']):
            return super(StoreView, self).update(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit stores.")

    def destroy(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, store_id=kwargs.get('pk')):
            return super(StoreView, self).destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit campaigns.")


@api_view(['GET'])
def store_gifts_view(request, store_id):
    return Response(get_gifts_by_store(request.user, int(store_id)), status=HTTP_200_OK)
