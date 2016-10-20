from HerculesApi.Auth.SignIn.functions import create_customer
from rest_framework.decorators import api_view


@api_view(['POST'])
def sign_in_view(request):
    create_customer(request)
