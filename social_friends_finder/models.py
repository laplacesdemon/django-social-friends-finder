from django.db import models
from utils import setting

if setting("SOCIAL_FRIENDS_USING_ALLAUTH", False):
    USING_ALLAUTH = True
    from allauth.socialaccount.models import SocialAccount as UserSocialAuth    
else:
    USING_ALLAUTH = False
    from social_auth.models import UserSocialAuth
from django.contrib.auth.models import User
from social_friends_finder.utils import SocialFriendsFinderBackendFactory


class SocialFriendsManager(models.Manager):

    def assert_user_is_social_auth_user(self, user):
        if not isinstance(user, UserSocialAuth):
            raise TypeError("user must be UserSocialAuth instance, not %s" % user)

    def fetch_social_friend_ids(self, social_auth_user):
        """
        fetches the user's social friends from its provider
        user is an instance of UserSocialAuth
        returns collection of ids

        this method can be used asynchronously as a background process (celery)
        """

        # Type check
        self.assert_user_is_social_auth_user(social_auth_user)

        # Get friend finder backend
        friends_provider = SocialFriendsFinderBackendFactory.get_backend(social_auth_user.provider)

        # Get friend ids
        friend_ids = friends_provider.fetch_friend_ids(social_auth_user)

        return friend_ids

    def existing_social_friends(self, user_social_auth=None, friend_ids=None):
        """
        fetches and matches social friends
        if friend_ids is None, then fetches them from social network

        Return:
            User collection
        """
        # Type check
        self.assert_user_is_social_auth_user(user_social_auth)

        if not friend_ids:
            friend_ids = self.fetch_social_friend_ids(user_social_auth)

        # Convert comma sepearated string to the list
        if isinstance(friend_ids, basestring):
            friend_ids = eval(friend_ids)

        # Match them with the ones on the website
        if USING_ALLAUTH:
            return User.objects.filter(socialaccount__uid__in=friend_ids).all()            
        else:
            return User.objects.filter(social_auth__uid__in=friend_ids).all()

    def get_or_create_with_social_auth(self, social_auth):
        """
        creates and saves model instance with collection of UserSocialAuth

        Raise:
            NotImplemetedError
        """
        # Type check
        self.assert_user_is_social_auth_user(social_auth)

        # Fetch the record
        try:
            social_friend_list = self.filter(user_social_auth=social_auth).get()
        except:
            # if no record found, create a new one
            friend_ids = self.fetch_social_friend_ids(social_auth)

            social_friend_list = SocialFriendList()
            social_friend_list.friend_ids = friend_ids
            social_friend_list.user_social_auth = social_auth
            social_friend_list.save()

        return social_friend_list

    def get_or_create_with_social_auths(self, social_auths):
        """
        creates and saves model instance with collection of UserSocialAuth

        Raise:
            NotImplemetedError
        """
        social_friend_coll = []
        for sa in social_auths:
            social_friend = self.get_or_create_with_social_auth(sa)
            social_friend_coll.append(social_friend)

        return social_friend_coll


class SocialFriendList(models.Model):

    user_social_auth = models.OneToOneField(UserSocialAuth, related_name="social_auth")
    friend_ids = models.CommaSeparatedIntegerField(max_length=10000000, blank=True, help_text="friends ids seperated by commas")

    objects = SocialFriendsManager()

    def __unicode__(self):
        return "%s on %s" % (self.user_social_auth.user.username, self.user_social_auth.provider)

    def existing_social_friends(self):
        return SocialFriendList.objects.existing_social_friends(self.user_social_auth, self.friend_ids)
