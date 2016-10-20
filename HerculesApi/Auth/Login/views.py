from httplib import OK
from django.contrib.auth import authenticate, login

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def login_view(request):
    user = authenticate(username=request.data['username'],
                        password=request.data['password'])
    if user is not None:
        login(request, user)
        return Response("Succefully logged in.",OK)
    return