from social_friends_finder.backends import BaseFriendsProvider
from social_friends_finder.utils import setting
if setting("SOCIAL_FRIENDS_USING_ALLAUTH", False):
    from social_auth.backends.facebook import FacebookBackend
    USING_ALLAUTH = False
else:
    from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
    USING_ALLAUTH = True
import facebook


class FacebookFriendsProvider(BaseFriendsProvider):

    def fetch_friends(self, user):
        """
        fethces friends from facebook using the oauth_token
        fethched by django-social-auth.

        Note - user isn't a user - it's a UserSocialAuth if using social auth, or a SocialAccount if using allauth

        Returns:
            collection of friend objects fetched from facebook
        """

        if USING_ALLAUTH:
            social_app = SocialApp.objects.get_current('facebook')
            oauth_token = SocialToken.objects.get(account=user, app=social_app).token
        else:
            social_auth_backend = FacebookBackend()

            # Get the access_token
            tokens = social_auth_backend.tokens(user)
            oauth_token = tokens['access_token']

        graph = facebook.GraphAPI(oauth_token)

        return graph.get_connections("me", "friends")

    def fetch_friend_ids(self, user):
        """
        fethces friend id's from facebook

        Return:
            collection of friend ids
        """
        friends = self.fetch_friends(user)
        friend_ids = []
        for friend in friends['data']:
            friend_ids.append(friend['id'])
        return friend_ids
