from django.conf.urls import patterns, url
from empleos import views

urlpatterns = patterns('',
                       url(r'^$', views.EmpleoListView.as_view(), name='index'),
                       url(r'^new$', views.EmpleoCreateView.as_view(), name='new'),
                       url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', views.EmpleoDetailView.as_view(), name='detail'),
)