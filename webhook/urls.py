from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webhooktest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^github/$', 'webhook.views.home', name='home'),
)
