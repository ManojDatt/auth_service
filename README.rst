auth_service
======================================

|build-status-image| |pypi-version|

Overview
--------

Authentication Service


Oauth2 django toolkit based aythentication.
    settings.py:


    INSTALLED_APPS = [
        '....',
        'oauth2_provider',
        'corsheaders',
        'rest_framework',
        'other - app',
    ]

    AUTH_SERVER_BASE_URL = "http://localhost:8000"
    AUTH_SERVER_CLIENT_ID = ""
    AUTH_SERVER_SECRET_KEY = ""
    # AUTH_SERVER_AUTH_TOKEN = ""
    OAUTH2_PROVIDER = {
        'RESOURCE_SERVER_INTROSPECTION_URL': f'{AUTH_SERVER_BASE_URL}/oauth/introspect/',
        # 'RESOURCE_SERVER_AUTH_TOKEN': AUTH_SERVER_AUTH_TOKEN,
        'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': (AUTH_SERVER_CLIENT_ID,AUTH_SERVER_SECRET_KEY),
        'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
    }


    AUTHENTICATION_BACKENDS = (
        'oauth2_provider.backends.OAuth2Backend',
        'django.contrib.auth.backends.ModelBackend',
    )

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
        ],
    }

Requirements
------------

-  Python (3.6>=)
-  Django (3.0>+)
-  Django REST Framework (3.1>=)

Installation
------------

Install using ``pip``\ …

.. code:: bash

    $ pip install auth_service

Example
-------

TODO: Write example.

Testing
-------

Install testing requirements.

.. code:: bash

    $ pip install -r requirements.txt

Run with runtests # https://packaging.python.org/tutorials/packaging-projects/

.. code:: bash

    $ ./runtests.py

You can also use the excellent `tox`_ testing tool to run the tests
against all supported versions of Python and Django. Install tox
globally, and then simply run:

.. code:: bash

    $ tox

Documentation
-------------

To build the documentation, you’ll need to install ``mkdocs``.

.. code:: bash

    $ pip install mkdocs

To preview the documentation:

.. code:: bash

    $ mkdocs serve
    Running at: http://127.0.0.1:8000/

To build the documentation:

.. code:: bash

    $ mkdocs build

.. _tox: http://tox.readthedocs.org/en/latest/

.. |build-status-image| image:: https://secure.travis-ci.org/ManojDatt/auth_service.svg?branch=master
   :target: http://travis-ci.org/ManojDatt/auth_service?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/auth_service.svg
   :target: https://pypi.python.org/pypi/auth_service
