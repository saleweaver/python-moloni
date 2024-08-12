PYTHON-MOLONI
==============

Welcome to the Moloni API Client! This Python package provides a simple and flexible way to interact with the Moloni API. It supports a wide range of endpoints and allows you to manage your Moloni account programmatically.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Documentation](#documentation)
- [Usage](#usage)
  - [Full Configuration](#full-configuration)
  - [Models as Entrypoints](#models-as-entrypoints)
  - [Minimal Configuration](#minimal-configuration)
- [Credentials](#credentials)
- [API Response Handling](#api-response-handling)
- [Supported Endpoints](#supported-endpoints)
- [License](#license)

## Features

- **Comprehensive Coverage:** Supports all Moloni API endpoints.
- **Flexible Configuration:** Easily configure and authenticate your requests.
- **Built-in Models:** Utilize predefined Pydantic models for request validation.


## Installation

You can install the Moloni API Client using pip:

```bash
pip install python-moloni
```

## Documentation

[Documentation is available here](https://python-moloni.readthedocs.io/en/latest/index.html)

## Usage

### Full Configuration

You can set up a fully configured client with all necessary authentication details:

```python
from moloni.api.companies_client import CompaniesClient
from moloni.base import AuthConfig, MoloniBaseUrl
import logging

logger = logging.getLogger(__name__)

companies = CompaniesClient(
    environment=MoloniBaseUrl.PROD,
    auth_config=AuthConfig(
        client_id="your_client_id",
        client_secret="your_client_secret",
        username="your_username",  # Optional if refresh_token is set
        password="your_password",  # Optional if refresh_token is set
        refresh_token="your_refresh_token",  # Optional if username and password are set
    ),
    log_level="INFO",
    version="v1",
    validate=True,
)
logger.info(companies.get_all())
```

### Models as Entrypoints

You can also use the predefined models as entrypoints to the API:

```python
from moloni.api import CustomersGetBySearchModel
from moloni.base import AuthConfig, MoloniBaseUrl
from pprint import pprint

auth_config = AuthConfig(
    client_id="your_client_id",
    client_secret="your_client_secret",
    username="your_username",  # Optional if refresh_token is set
    password="your_password",  # Optional if refresh_token is set
    refresh_token="your_refresh_token",  # Optional if username and password are set
)

with CustomersGetBySearchModel(company_id=5, search="cafe").connect(
    auth_config=auth_config
) as api:
    pprint(api.request().payload)
    
```


### Minimal Configuration

For a minimal setup, credentials can be passed via environment variables:

```python
from moloni.api.companies_client import CompaniesClient
from moloni.api.products_client import ProductsClient, ProductsGetAllModel
import logging 

logger = logging.getLogger(__name__)

companies = CompaniesClient()
logger.info(companies.get_all())
products = ProductsClient()
logger.info(products.get_all(dict(company_id=5, category_id=8231525)))

product = products.insert(
    dict(
        company_id=5,
        category_id=123456,
        unit_id=134568,
        has_stock="0",
        name="Name",
        reference="Reference",
        price="10",
        type="1",
        taxes=[{"tax_id": 123455, "order": 0, "cumulative": 0}],
    )
)

#  or with a model

products_response = products.get_all(
    ProductsGetAllModel(company_id=5, category_id=8231525)
)
```

## Credentials

### Passing Credentials

You can pass your credentials directly in the code or via environment variables:

```python
from moloni.base import AuthConfig

auth_config = AuthConfig(
    client_id='your_client_id',
    client_secret='your_client_secret',
    username='your_username',
    password='your_password',
    refresh_token='your_refresh_token'
)
```

### Environment Variables

Alternatively, set the following environment variables:

```bash
export MOLONI_CLIENT_ID="your_client_id"
export MOLONI_CLIENT_SECRET="your_client_secret"
export MOLONI_REFRESH_TOKEN="your_refresh_token"
export MOLONI_USERNAME="your_username"
export MOLONI_PASSWORD="your_password"
```

## API Response Handling

The API responses are encapsulated in an ApiResponse object, which provides methods to access the response payload and handle pagination.

### Example:

```python
response = companies.get_all()
print(response.payload)  # Access the JSON payload
print(response.status_code)  # Check the HTTP status code

try:
    next_page = response.next(qty=10)
    print("Fetching next page with:", next_page)
except NoMoreRecords:
    print("No more records to fetch.")
```

## Supported Endpoints

This client supports the full list of Moloni API endpoints, including:

	•	BankaccountsClient
	•	BillsofladingClient
	•	CompaniesClient
	•	CustomersClient
	•	InvoicesClient
	•	ProductsClient
	•	WarehousesClient

For a full list, please refer to the [documentation](https://python-moloni.readthedocs.io/en/latest/index.html).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

-------

[![Coverage](./coverage.svg)](./coverage.svg)

-------

##### Disclaimer

We are not affiliated with Moloni, this is an unofficial wrapper to access their API. For more information, please visit their [official website](https://www.moloni.pt/).
