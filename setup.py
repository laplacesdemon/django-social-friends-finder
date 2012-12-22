# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-social-friends-finder',
    version='0.2',
    author=u'Suleyman Melikoglu',
    author_email='suleyman@melikoglu.info',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/laplacesdemon/django-social-friends-finder.git',
    license='BSD licence, see LICENCE.txt',
    description='An extension app for django-social-auth or django-allauth that fetches your friends from different social-networks.',
    long_description=open('README.md').read(),
    zip_safe=False,
)
