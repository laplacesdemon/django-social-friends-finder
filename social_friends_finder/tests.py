"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from social_auth.models import UserSocialAuth
from django.contrib.auth.models import User
from social_friends_finder.models import SocialFriendList
from django.test.client import Client


class SocialFriendsManagerTest(TestCase):

    fixtures = ['users.json', 'social_auth.json']

    def setUp(self):
        pass

    def test_fixtures(self):
        """making sure that fixtures are working"""
        users = User.objects.all()
        self.assertEqual(len(users), 2)

        social_users = UserSocialAuth.objects.all()
        self.assertEqual(len(social_users), 2)

    def test_fetch_friends_from_twitter(self):
        """tests that we can fetch friend ids"""
        usa = UserSocialAuth.objects.all()[0]
        friend_ids = SocialFriendList.objects.fetch_social_friend_ids(usa)

        # assert that we have at least 1 friend
        self.assertTrue(len(friend_ids) > 0)

    def test_existing_social_friend_on_website(self):
        """
        """
        usa = UserSocialAuth.objects.all()[0]
        friends = SocialFriendList.objects.existing_social_friends(usa)

        self.assertTrue(len(friends), 1)
        user = friends[0]
        self.assertIsInstance(user, User)
        user_social = user.social_auth.all()[0]
        self.assertEqual(user_social.provider, "twitter")
        self.assertEqual(user.pk, 2)
        self.assertEqual(user.username, "admin")

    def test_create_with_social_auth(self):
        usa = UserSocialAuth.objects.all()[0]
        social_friend = SocialFriendList.objects.get_or_create_with_social_auth(usa)

        self.assertTrue(len(social_friend.friend_ids) > 0)


class SocialFriendListViewTest(TestCase):

    fixtures = ['users.json', 'social_auth.json']

    def setUp(self):
        pass

    def test_view_returns_friends(self):
        client = Client()
        client.login(username="laplaces_demon", password="12345678")
        res = client.get("/find-friends/list/")

        self.assertEqual(200, res.status_code)
        friends = res.context['friends']
        self.assertEqual(1, len(friends))
        self.assertEqual("admin", friends[0].username)
        self.assertEqual('twitter', res.context['connected_providers'][0])
