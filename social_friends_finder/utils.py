from django.conf import settings


class SocialFriendsFinderBackendFactory():

    @classmethod
    def get_backend(self, backend_name):
        """
        returns the given backend instance
        """
        if backend_name == 'twitter':
            from social_friends_finder.backends.twitter_backend import TwitterFriendsProvider
            friends_provider = TwitterFriendsProvider()
        elif backend_name == 'facebook':
            from social_friends_finder.backends.facebook_backend import FacebookFriendsProvider
            friends_provider = FacebookFriendsProvider()
        else:
            raise NotImplementedError("provider: %s is not implemented")

        return friends_provider


def setting(name, default=None):
    """returns the setting value or default if not exists"""
    return getattr(settings, name, default)
