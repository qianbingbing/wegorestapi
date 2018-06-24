from django.conf.urls import url
from wegoapi import views

urlpatterns = [
    url(r'^wego/$', views.snippet_list),
    url(r'^wego/(?P<pk>[0-9]+)/$', views.snippet_detail),
]