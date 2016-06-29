from rest_framework import viewsets

from HerculesApi.Card.model import Card
from HerculesApi.Card.serializer import CardSerializer


class CardsView(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()