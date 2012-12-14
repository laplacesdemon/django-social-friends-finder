class BaseFriendsProvider():

    def fetch_friends(self, user):
        """abstract method"""
        raise NotImplementedError("Should have implemented this")

    def fetch_friend_ids(self, user):
        """abstract method"""
        raise NotImplementedError("Should have implemented this")
