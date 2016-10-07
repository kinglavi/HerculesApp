from rest_framework import viewsets

from HerculesApi.Sticker.model import Sticker
from HerculesApi.Sticker.serializer import StickerSerializer


class StickersView(viewsets.ModelViewSet):
    """
        This is product view set.
    """
    serializer_class = StickerSerializer
    queryset = Sticker.objects.all()
    # permission_class = ONLY_ADMINS