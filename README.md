django-social-friends-finder
============================

An extension for django-social-auth that finds matched friends on connected social network and your websit
It displays matched friends so you can suggest your users to add them as friend or follow them. 

Dependencies
------------

  * django-social-auth>=0.7.10 and all its dependencies https://github.com/omab/django-social-auth.git
  * python-twitter>=0.8.2 for twitter backend http://code.google.com/p/python-twitter/
  * facebook-sdk for facebook backend https://github.com/pythonforfacebook/facebook-sdk.git

Installation
------------

There are 3 ways to install this app

@todo pypi

or build from the source.

    python setup.py install

or add `social_friends_finder` to your path

Usage and Configuration
-----------------------

Add `social_friends_finder` to your APPS list in your settings file

    INSTALLED_APPS = (
        ...
        "social_friends_finder",
    )

Add urls to your url config

    urlpatterns = patterns('',
        ...
        url(r'^find-friends/', include('social_friends_finder.urls')),
    )

Optionally you can use following settings:

    `SF_REDIRECT_IF_NO_SOCIAL_ACCOUNT_FOUND`: True if no social account found. Default is True
    `REDIRECT_URL`: The url to redirect if above setting is used. Default is "/"

Go to `/find-friends/list/` on your browser.

Contributions
-------------

Currently there are facebook, twitter and google-oauth2 backends are available. Please help to implement new backends.

Implementing backend classes are easy. Just create a class inherits from `BaseFriendsProvider` and implement two of its methods. 
See backends module for example implementations
