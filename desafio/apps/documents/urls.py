from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /documents/5/
    url(r'^(?P<document_id>\d+)/$', views.detail, name='detail'),
)