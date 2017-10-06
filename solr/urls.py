from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    # new url definition
    url(r'^solrquery/$', views.solrquery, name='solrquery'),
]
