#!/usr/bin/env python
import sys
import os

from django.conf import settings
from django.core.management import call_command

BASE_DIR = os.path.dirname(__file__)


def runtests():
    if not settings.configured:
        # Configure test environment
        settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:'
                }
            },
            SITE_ID=1,
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.admin',
                'password_session',
            ),
            AUTHENTICATION_BACKENDS = (
                'django.contrib.auth.backends.ModelBackend',
            ),
            MIDDLEWARE_CLASSES = (
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'password_session.middleware.CheckPasswordHash',
            ),
            ROOT_URLCONF = 'password_session.tests.test_urls',
            LANGUAGES = (
                ('en', 'English'),
            ),
        )

    failures = call_command('test', 'password_session', interactive=False, failfast=False, verbosity=2)
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
