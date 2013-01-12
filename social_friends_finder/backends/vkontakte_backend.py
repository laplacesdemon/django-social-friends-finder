from social_friends_finder.backends import BaseFriendsProvider
from social_friends_finder.utils import setting
if not setting("SOCIAL_FRIENDS_USING_ALLAUTH", False):
    from social_auth.backends.contrib.vkontakte import VKontakteOAuth2Backend
    USING_ALLAUTH = False
else:
    from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
    USING_ALLAUTH = True
import vkontakte


class VKontakteFriendsProvider(BaseFriendsProvider):

    def fetch_friends(self, user):
        """
        fethces friends from VKontakte using the access_token
        fethched by django-social-auth.

        Note - user isn't a user - it's a UserSocialAuth if using social auth, or a SocialAccount if using allauth

        Returns:
            collection of friend objects fetched from VKontakte
        """

        if USING_ALLAUTH:
            raise NotImplementedError("VKontakte support is not implemented for django-allauth")
            #social_app = SocialApp.objects.get_current('vkontakte')
            #oauth_token = SocialToken.objects.get(account=user, app=social_app).token
        else:
            social_auth_backend = VKontakteOAuth2Backend()

            # Get the access_token
            tokens = social_auth_backend.tokens(user)
            oauth_token = tokens['access_token']

        api = vkontakte.API(token=oauth_token)
        return api.get("friends.get")

    def fetch_friend_ids(self, user):
        """
        fetches friend id's from vkontakte

        Return:
            collection of friend ids
        """
        friend_ids = self.fetch_friends(user)
        return friend_ids
