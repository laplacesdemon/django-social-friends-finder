from django.conf.urls import patterns, url
from social_friends_finder.views import FriendListView

urlpatterns = patterns('social_friends_finder.views',
    url(r'^list/$', FriendListView.as_view(), name='friend_list'),
    url(r'^list/(?P<provider>[\w.@+-]+)/$', FriendListView.as_view(), name='friend_list'),
)
