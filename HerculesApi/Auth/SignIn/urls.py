from HerculesApi.Auth.SignIn.views import sign_in_view
from django.conf.urls import url

urlpatterns = [
    url(r'^sign_in/$', sign_in_view),
]
