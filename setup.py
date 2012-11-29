# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-social-friends-finder',
    version='0.1',
    author=u'Suleyman Melikoglu',
    author_email='suleyman@melikoglu.info',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/laplacesdemon/django-social-friends-finder.git',
    license='BSD licence, see LICENCE.txt',
    description='An extension for django-social-auth that finds matched friends on connected social network and your website.',
    long_description=open('README.md').read(),
    zip_safe=False,
)
