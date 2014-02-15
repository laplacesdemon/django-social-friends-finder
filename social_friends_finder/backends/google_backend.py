import feedparser
import gdata.gauth
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

from django.conf import settings

from social_auth.backends.google import GoogleOAuth2Backend
from social_friends_finder.backends import BaseFriendsProvider

if getattr(settings, "SOCIAL_FRIENDS_USING_ALLAUTH", False):
    from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
    USING_ALLAUTH = True
else:
    USING_ALLAUTH = False


class GoogleFriendsProvider(BaseFriendsProvider):

    def fetch_friends(self, user):
        """
        fetches the friends from g+ using the
        information on django-social-auth models
        user is an instance of UserSocialAuth.
        Notice that g+ contact api should be enabled in
        google cloud console and social auth scope has been set
        this way in settings.py

        GOOGLE_OAUTH_EXTRA_SCOPE = ['https://www.google.com/m8/feeds/']

        Returns:
            collection of friend data dicts fetched from google contact api
        """

        if USING_ALLAUTH:
            social_app = SocialApp.objects.get_current('google')
            oauth_token = SocialToken.objects.get(account=user, app=social_app).token
        else:
            social_auth_backend = GoogleOAuth2Backend()
            # Get the access_token
            tokens = social_auth_backend.tokens(user)
            oauth_token = tokens['access_token']

        credentials = gdata.gauth.OAuth2Token(
            client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
            client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            scope='https://www.google.com/m8/feeds/',
            user_agent='gdata',
            access_token=oauth_token
        )
        client = gdata.contacts.client.ContactsClient()
        credentials.authorize(client)
        contacts = client.get_contacts()
        data = feedparser.parse(contacts.to_string())['entries']

        return data

    def fetch_friend_ids(self, user):
        """
        fetches friend email's from g+

        Return:
            collection of friend emails (ids)
        """
        friends = self.fetch_friends(user)

        return [friend['ns1_email']['address']
                for friend in friends
                if 'ns1_email' in friend]
