Example Project
===============

This is a sample project to test out `social-friends-finder`
This example app is using `django-social-auth` for its social authentication

Installation
------------

Install virtualenv if it's not installed before

    pip install virtualenv

Use following to set up the project

    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt

Configuration
-------------

Please see configuration steps on `django-social-auth`. In short you have to set following settings in `settings.py`

    TWITTER_CONSUMER_KEY         
    TWITTER_CONSUMER_SECRET      
    FACEBOOK_APP_ID              
    FACEBOOK_API_SECRET          
