from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^account/list$', views.list_accounts, name='list_accounts'),
    url(r'^account/search$', views.search_accounts, name='search_accounts'),
    url(r'^account/(?P<account_id>[0-9]+)/add$', views.add, name='add'),
    url(r'^account/(?P<account_id>[0-9]+)/subtract$', views.subtract, name='subtract'),
]
