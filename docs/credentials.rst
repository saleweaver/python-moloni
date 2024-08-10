Credentials
===========

You can pass your credentials multiple ways, use one of them.
The order of searching for credentials is:

1. Parameters passed from code
2. Environment variables



.. code-block:: python

    from moloni.base import AuthConfig

    auth_config = AuthConfig(
        client_id='your_client_id',
        client_secret='your_client_secret',
        username='your_username',
        password='your_password',
        refresh_token='your_refresh_token'
    )

Environment variables
---------------------


.. code-block:: python

    client_id: str = os.getenv("MOLONI_CLIENT_ID")
    client_secret: str = os.getenv("MOLONI_CLIENT_SECRET")
    refresh_token: str = os.getenv("MOLONI_REFRESH_TOKEN")
    username: str = os.getenv("MOLONI_USERNAME")
    password: str = os.getenv("MOLONI_PASSWORD")

