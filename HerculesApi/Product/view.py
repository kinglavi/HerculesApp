from HerculesApi.Permissions.permissions import is_admin_or_company_manager
from HerculesApi.Product.functions import get_products_by_user
from HerculesApi.Product.model import Product
from HerculesApi.Product.serializer import ProductSerializer
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated


class ProductView(viewsets.ModelViewSet):
    """
        This is product view set.
    """
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_products_by_user(self.request.user)

    def create(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, store_id=request.data['store']):
            return super(ProductView, self).create(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can create stores.")

    def update(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, store_id=request.data['store']):
            return super(ProductView, self).update(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit stores.")

    def destroy(self, request, *args, **kwargs):
        if is_admin_or_company_manager(request.user, product_id=kwargs.get('pk')):
            return super(ProductView, self).destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied("Only the manager of the company can edit campaigns.")

    def perform_create(self, serializer):
        # TODO: check that data doesnt have value for sticker counter.(Must start with 0)
        pass
        super(ProductView, self).perform_create(serializer)
