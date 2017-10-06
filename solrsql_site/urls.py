from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'solrsql_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^solrquery/$', 'solr.views.solrquery', name='solrquery'),
    url(r'^solr/', include('solr.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
