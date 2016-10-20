from HerculesApi.Auth.Login.views import login_view
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', login_view),
    # url(r'^logout/$', logout_view)
]
