from django.conf.urls import url, include

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('HerculesApi.Campaign.urls')),
    url(r'^api/', include('HerculesApi.Product.urls')),
    url(r'^api/', include('HerculesApi.Company.urls')),
    url(r'^api/', include('HerculesApi.Sticker.urls')),
    url(r'^api/', include('HerculesApi.Customer.urls')),
    url(r'^api/', include('HerculesApi.Card.urls')),
    url(r'^api/', include('HerculesApi.Store.urls')),
    url(r'^api-auth/', include('HerculesApi.Auth.urls'))
    # url(r'^api/', include('HerculesApi.Group.urls')),
]
