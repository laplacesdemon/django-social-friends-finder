from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'', include('social_auth.urls')),
    url(r'^find-friends/', include('social_friends_finder.urls')),
)
