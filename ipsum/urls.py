from django.conf.urls import patterns, include, url

from .views import IpsumHomeView

urlpatterns = patterns('',

    url(r'^$', IpsumHomeView.as_view(), name='home'),
)
