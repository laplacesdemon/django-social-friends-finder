from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),

    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/', include('allauth.urls')),
    url(r'^find-friends/', include('social_friends_finder.urls')),
)
