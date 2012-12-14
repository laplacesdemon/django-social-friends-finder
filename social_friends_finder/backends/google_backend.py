from social_friends_finder.backends import BaseFriendsProvider


# see: http://djangosnippets.org/snippets/706/
class GoogleFriendsProvider(BaseFriendsProvider):

    def fetch_friends(self, user):
        return None

    def fetch_friend_ids(self, user):
        """not implemented yet"""
        return []
