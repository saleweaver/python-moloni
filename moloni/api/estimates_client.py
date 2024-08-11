from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = EstimatesClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class Associated_documents(BaseModel):
    associated_id: Optional[Any] = None
    value: Optional[Any] = None


class Payments(BaseModel):
    date: Optional[Any] = None
    notes: Optional[Any] = None
    payment_method_id: Optional[Any] = None
    value: Optional[Any] = None


class Products(BaseModel):
    discount: Optional[Any] = None
    exemption_reason: Optional[Any] = None
    name: Optional[Any] = None
    order: Optional[Any] = None
    price: Optional[Any] = None
    product_id: Optional[Any] = None
    qty: Optional[Any] = None
    summary: Optional[Any] = None
    taxes: Optional[Any] = None
    warehouse_id: Optional[Any] = None


class EstimatesCountModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    number: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    year: Optional[str] = None
    your_reference: Optional[str] = None

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.count(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class EstimatesDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    document_id: Optional[Union[str, int]] = None

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.delete(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class EstimatesGetAllModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    number: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25
    salesman_id: Optional[Union[str, int]] = None
    year: Optional[str] = None
    your_reference: Optional[str] = None

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.get_all(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class EstimatesGetOneModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    number: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    year: Optional[str] = None
    your_reference: Optional[str] = None

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.get_one(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class EstimatesInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    deduction_id: Optional[Union[str, int]] = None
    delivery_datetime: Optional[str] = None
    delivery_departure_address: Optional[str] = None
    delivery_departure_city: Optional[str] = None
    delivery_departure_country: Optional[str] = None
    delivery_departure_zip_code: Optional[str] = None
    delivery_destination_address: Optional[str] = None
    delivery_destination_city: Optional[str] = None
    delivery_destination_country: Optional[str] = None
    delivery_destination_zip_code: Optional[str] = None
    delivery_method_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    financial_discount: Optional[str] = None
    notes: Optional[str] = None
    products: Optional[List[Products]] = None
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    special_discount: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[Union[str, int]] = None
    your_reference: Optional[str] = None

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.insert(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class EstimatesUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    deduction_id: Optional[Union[str, int]] = None
    delivery_datetime: Optional[str] = None
    delivery_departure_address: Optional[str] = None
    delivery_departure_city: Optional[str] = None
    delivery_departure_country: Optional[str] = None
    delivery_departure_zip_code: Optional[str] = None
    delivery_destination_address: Optional[str] = None
    delivery_destination_city: Optional[str] = None
    delivery_destination_country: Optional[str] = None
    delivery_destination_zip_code: Optional[str] = None
    delivery_method_id: Optional[Union[str, int]] = None
    document_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    financial_discount: Optional[str] = None
    notes: Optional[str] = None
    products: Optional[List[Products]] = None
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    special_discount: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[Union[str, int]] = None
    your_reference: Optional[str] = None

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.update(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class EstimatesClient(MoloniBaseClient):

    @endpoint("/<version>/estimates/count/", method="post")
    def count(self, data: Union[EstimatesCountModel, dict], **kwargs):
        """
        count(self, data: Union[EstimatesCountModel, dict], **kwargs)

        Args:

            data (Union[EstimatesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesCountModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesCountModel.

                - date (str): date of the EstimatesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesCountModel.

                - expiration_date (str): expiration_date of the EstimatesCountModel.

                - number (str): number of the EstimatesCountModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesCountModel.

                - year (str): year of the EstimatesCountModel.

                - your_reference (str): your_reference of the EstimatesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/delete/", method="post")
    def delete(self, data: Union[EstimatesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[EstimatesDeleteModel, dict], **kwargs)

        Args:

            data (Union[EstimatesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesDeleteModel.

                - document_id (Union[str, int]): document_id of the EstimatesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/getAll/", method="post")
    def get_all(self, data: Union[EstimatesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[EstimatesGetAllModel, dict], **kwargs)

        Args:

            data (Union[EstimatesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesGetAllModel.

                - date (str): date of the EstimatesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesGetAllModel.

                - expiration_date (str): expiration_date of the EstimatesGetAllModel.

                - number (str): number of the EstimatesGetAllModel.

                - offset (str): offset of the EstimatesGetAllModel.

                - qty (str): qty of the EstimatesGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesGetAllModel.

                - year (str): year of the EstimatesGetAllModel.

                - your_reference (str): your_reference of the EstimatesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/getOne/", method="post")
    def get_one(self, data: Union[EstimatesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[EstimatesGetOneModel, dict], **kwargs)

        Args:

            data (Union[EstimatesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesGetOneModel.

                - date (str): date of the EstimatesGetOneModel.

                - document_id (Union[str, int]): document_id of the EstimatesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesGetOneModel.

                - expiration_date (str): expiration_date of the EstimatesGetOneModel.

                - number (str): number of the EstimatesGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesGetOneModel.

                - year (str): year of the EstimatesGetOneModel.

                - your_reference (str): your_reference of the EstimatesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/insert/", method="post")
    def insert(self, data: Union[EstimatesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[EstimatesInsertModel, dict], **kwargs)

        Args:

            data (Union[EstimatesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesInsertModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesInsertModel.

                - date (str): date of the EstimatesInsertModel.

                - deduction_id (Union[str, int]): deduction_id of the EstimatesInsertModel.

                - delivery_datetime (str): delivery_datetime of the EstimatesInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the EstimatesInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the EstimatesInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the EstimatesInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the EstimatesInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the EstimatesInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the EstimatesInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the EstimatesInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the EstimatesInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the EstimatesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesInsertModel.

                - expiration_date (str): expiration_date of the EstimatesInsertModel.

                - financial_discount (str): financial_discount of the EstimatesInsertModel.

                - notes (str): notes of the EstimatesInsertModel.

                - products (str): products of the EstimatesInsertModel.

                - salesman_commission (str): salesman_commission of the EstimatesInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesInsertModel.

                - special_discount (str): special_discount of the EstimatesInsertModel.

                - status (str): status of the EstimatesInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the EstimatesInsertModel.

                - your_reference (str): your_reference of the EstimatesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/update/", method="post")
    def update(self, data: Union[EstimatesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[EstimatesUpdateModel, dict], **kwargs)

        Args:

            data (Union[EstimatesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesUpdateModel.

                - date (str): date of the EstimatesUpdateModel.

                - deduction_id (Union[str, int]): deduction_id of the EstimatesUpdateModel.

                - delivery_datetime (str): delivery_datetime of the EstimatesUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the EstimatesUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the EstimatesUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the EstimatesUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the EstimatesUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the EstimatesUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the EstimatesUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the EstimatesUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the EstimatesUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the EstimatesUpdateModel.

                - document_id (Union[str, int]): document_id of the EstimatesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesUpdateModel.

                - expiration_date (str): expiration_date of the EstimatesUpdateModel.

                - financial_discount (str): financial_discount of the EstimatesUpdateModel.

                - notes (str): notes of the EstimatesUpdateModel.

                - products (str): products of the EstimatesUpdateModel.

                - salesman_commission (str): salesman_commission of the EstimatesUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesUpdateModel.

                - special_discount (str): special_discount of the EstimatesUpdateModel.

                - status (str): status of the EstimatesUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the EstimatesUpdateModel.

                - your_reference (str): your_reference of the EstimatesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
