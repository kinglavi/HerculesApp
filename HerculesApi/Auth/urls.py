from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', views.login, template_name, name='login'),
    url(r'^logout/$', views.logout, template_name, name='logout'),
]
