from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from HerculesApi.Card.functions import increase_card_punch_counter, get_cards_queryset_by_user, get_all_cards_by_store, \
    get_all_cards_by_company
from HerculesApi.Card.model import Card
from HerculesApi.Card.serializer import CardSerializer
from HerculesApi.Permissions.permissions import IsAdminOrReadOnly, is_admin_or_company_manager


class CardsView(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        return get_cards_queryset_by_user(self.request.user)


@api_view(['GET'])
def get_all_cards_by_store_view(request, store_id):
    if is_admin_or_company_manager(request.user, store_id=store_id,
                                   include_workers=True):
        return Response(get_all_cards_by_store(store_id).values(), status=HTTP_200_OK)
    else:
        raise PermissionDenied("Only workers in the store or company managers can see the cards in the store.")


@api_view(['GET'])
def get_all_cards_by_company_view(request, company_id):
    if is_admin_or_company_manager(request.user, company_id=True):
        return Response(get_all_cards_by_company(company_id).values(), status=HTTP_200_OK)
    else:
        raise PermissionDenied("Only managers of the company can see the cards in the store.")


@api_view(['POST'])
def increase_card_counter_view(request):
    """
        Increase the punch_counter if the reqeust user is the owner of the card or
        the reques user is superuser
    :param request:
    :return: If success return 201
    """
    try:
        increase_card_punch_counter(request.user, request.data['token'])
    except Exception as e:
        if e.detail[0]:
            raise APIException(e.detail[0])
        else:
            raise APIException("Error occurred increasing punch counter of card.")
    return Response("Counter raised.", status=HTTP_200_OK)
