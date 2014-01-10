=======================
Django Password Session
=======================

A reusable Django app that will invalidate all active sessions after change password.

.. image:: https://badge.fury.io/py/django-password-session.png
   :target: http://badge.fury.io/py/django-password-session

.. image:: https://api.travis-ci.org/alikus/django-password-session.png
   :target: https://travis-ci.org/alikus/django-password-session

.. image:: https://coveralls.io/repos/alikus/django-password-session/badge.png?branch=master
    :target: https://coveralls.io/r/alikus/django-password-session?branch=master

Installation
------------

1. Install a package.

.. code-block:: bash

    $ pip install django-password-session

2. Add "password_session" to your INSTALLED_APPS setting:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'password_session',
    )

3. Add middleware:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'password_session.middleware.CheckPasswordHash',
    ),

4. Make sure that you have the following settings:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
    )

    AUTHENTICATION_BACKENDS = (
        ...
        'django.contrib.auth.backends.ModelBackend',
    )

    MIDDLEWARE_CLASSES = (
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    )

5. To avoid logging out from a current session you should call the following signal directly after change password:

.. code-block:: python

    from password_session.signals import password_changed
    password_changed.send(sender=user.__class__, user=user, request=request)

Example view
------------

It's a very simple view for change password just for demonstrating how to call the signal.
In real situation this view should be more complicated.

.. code-block:: python

    from django.contrib.auth.decorators import login_required
    from django.http import HttpResponse
    
    from password_session.signals import password_changed
    
    
    @login_required(login_url='/admin/')
    def change_password_view(request):
        user = request.user
        user.set_password(request.POST.get('password'))
        user.save()
        password_changed.send(sender=user.__class__, user=user, request=request)
        return HttpResponse("Hello, %s! Your password has been changed!" % user.username)

Settings
--------
Default application settings can be overriden in settings.py:

.. code-block:: python

    PASSWORD_SESSION_PASSWORD_HASH_KEY = 'password_session_password_hash_key' #  default key stored in session
    PASSWORD_SESSION_PASSWORD_HASH_LENGTH = 4 #  default key length

Requirements
------------

* Python 2.6+ or 3+
* Django 1.3+
