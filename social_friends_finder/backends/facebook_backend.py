from social_friends_finder.backends import BaseFriendsProvider
from social_auth.backends.facebook import FacebookBackend
import facebook


class FacebookFriendsProvider(BaseFriendsProvider):

    def fetch_friends(self, user):
        """
        fethces friends from facebook using the oauth_token
        fethched by django-social-auth.

        Returns:
            collection of friend objects fetched from facebook
        """
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
