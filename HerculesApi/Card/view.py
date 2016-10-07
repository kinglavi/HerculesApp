from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from HerculesApi.Card.functions import increase_card_punch_counter, get_cards_queryset_by_user
from HerculesApi.Card.model import Card
from HerculesApi.Card.serializer import CardSerializer
from HerculesApi.Permissions.permissions import IsAdminOrReadOnly


class CardsView(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        return get_cards_queryset_by_user(self.request.user)


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
            raise APIException("Error occurred increasing punch counter of card." )
    return Response("Counter raised.", status=HTTP_200_OK)
