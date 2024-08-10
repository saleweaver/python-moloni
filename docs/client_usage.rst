Client Usage
============






All endpoint's clients have the following signature and default values:



.. code-block:: python

    from moloni.api.companies_client import CompaniesClient
    from moloni.base import AuthConfig, MoloniBaseUrl
    import logging

    logger = logging.getLogger(__name__)


    companies = CompaniesClient(
        environment=MoloniBaseUrl.PROD,
        auth_config=AuthConfig(
            client_id='your_client_id',
            client_secret='your_client_secret',
            username='your_username', # Optional if refresh_token is set
            password='your_password', # Optional if refresh_token is set
            refresh_token='your_refresh_token' # Optional if username and password are set
        ),
        log_level='INFO',
        version='v1',
        validate=True
    )
    logger.info(companies.get_all())



Minimal configuration, with credentials set as environment variables
---------------------------------------------------------------------


.. code-block:: python

    from moloni.api.companies_client import CompaniesClient
    from moloni.api.products_client import ProductsClient
    import logging

    logger = logging.getLogger(__name__)


    companies = CompaniesClient()
    logger.info(companies.get_all())
    products = ProductsClient()
    logger.info(products.get_all(dict(company_id=5, category_id=8231525)))



