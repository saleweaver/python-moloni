from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = WaybillsClient(*args, **kwargs)
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


class WaybillsCountModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
    number: Optional[str] = None
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


class WaybillsDeleteModel(ApiRequestModel):
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


class WaybillsGetAllModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
    number: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25
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


class WaybillsGetOneModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    number: Optional[str] = None
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


class WaybillsInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    associated_documents: Optional[List[Associated_documents]] = None
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
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
    financial_discount: Optional[str] = None
    notes: Optional[str] = None
    products: Optional[List[Products]] = None
    related_documents_notes: Optional[str] = None
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


class WaybillsSetTransportCodeModel(ApiRequestModel):
    company_id: Union[str, int]
    document_id: Optional[Union[str, int]] = None
    transport_code: Optional[str] = None

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
            response = self._api_client.set_transport_code(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class WaybillsUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    associated_documents: Optional[List[Associated_documents]] = None
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
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
    financial_discount: Optional[str] = None
    notes: Optional[str] = None
    products: Optional[List[Products]] = None
    related_documents_notes: Optional[str] = None
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


class WaybillsClient(MoloniBaseClient):

    @endpoint("/<version>/waybills/count/", method="post")
    def count(self, data: Union[WaybillsCountModel, dict], **kwargs):
        """
        count(self, data: Union[WaybillsCountModel, dict], **kwargs)

        Args:

            data (Union[WaybillsCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsCountModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsCountModel.

                - date (str): date of the WaybillsCountModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsCountModel.

                - number (str): number of the WaybillsCountModel.

                - year (str): year of the WaybillsCountModel.

                - your_reference (str): your_reference of the WaybillsCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/delete/", method="post")
    def delete(self, data: Union[WaybillsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[WaybillsDeleteModel, dict], **kwargs)

        Args:

            data (Union[WaybillsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsDeleteModel.

                - document_id (Union[str, int]): document_id of the WaybillsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/getAll/", method="post")
    def get_all(self, data: Union[WaybillsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[WaybillsGetAllModel, dict], **kwargs)

        Args:

            data (Union[WaybillsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsGetAllModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsGetAllModel.

                - date (str): date of the WaybillsGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsGetAllModel.

                - number (str): number of the WaybillsGetAllModel.

                - offset (str): offset of the WaybillsGetAllModel.

                - qty (str): qty of the WaybillsGetAllModel.

                - year (str): year of the WaybillsGetAllModel.

                - your_reference (str): your_reference of the WaybillsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/getOne/", method="post")
    def get_one(self, data: Union[WaybillsGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[WaybillsGetOneModel, dict], **kwargs)

        Args:

            data (Union[WaybillsGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsGetOneModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsGetOneModel.

                - date (str): date of the WaybillsGetOneModel.

                - document_id (Union[str, int]): document_id of the WaybillsGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsGetOneModel.

                - number (str): number of the WaybillsGetOneModel.

                - year (str): year of the WaybillsGetOneModel.

                - your_reference (str): your_reference of the WaybillsGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/insert/", method="post")
    def insert(self, data: Union[WaybillsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[WaybillsInsertModel, dict], **kwargs)

        Args:

            data (Union[WaybillsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the WaybillsInsertModel.

                - company_id (Union[str, int]): company_id of the WaybillsInsertModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsInsertModel.

                - date (str): date of the WaybillsInsertModel.

                - delivery_datetime (str): delivery_datetime of the WaybillsInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the WaybillsInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the WaybillsInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the WaybillsInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the WaybillsInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the WaybillsInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the WaybillsInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the WaybillsInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the WaybillsInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the WaybillsInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsInsertModel.

                - financial_discount (str): financial_discount of the WaybillsInsertModel.

                - notes (str): notes of the WaybillsInsertModel.

                - products (str): products of the WaybillsInsertModel.

                - related_documents_notes (str): related_documents_notes of the WaybillsInsertModel.

                - status (str): status of the WaybillsInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the WaybillsInsertModel.

                - your_reference (str): your_reference of the WaybillsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/setTransportCode/", method="post")
    def set_transport_code(
        self, data: Union[WaybillsSetTransportCodeModel, dict], **kwargs
    ):
        """
        set_transport_code(self, data: Union[WaybillsSetTransportCodeModel, dict], **kwargs)

        Args:

            data (Union[WaybillsSetTransportCodeModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsSetTransportCodeModel.

                - document_id (Union[str, int]): document_id of the WaybillsSetTransportCodeModel.

                - transport_code (str): transport_code of the WaybillsSetTransportCodeModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsSetTransportCodeModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/update/", method="post")
    def update(self, data: Union[WaybillsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[WaybillsUpdateModel, dict], **kwargs)

        Args:

            data (Union[WaybillsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the WaybillsUpdateModel.

                - company_id (Union[str, int]): company_id of the WaybillsUpdateModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsUpdateModel.

                - date (str): date of the WaybillsUpdateModel.

                - delivery_datetime (str): delivery_datetime of the WaybillsUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the WaybillsUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the WaybillsUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the WaybillsUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the WaybillsUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the WaybillsUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the WaybillsUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the WaybillsUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the WaybillsUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the WaybillsUpdateModel.

                - document_id (Union[str, int]): document_id of the WaybillsUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsUpdateModel.

                - financial_discount (str): financial_discount of the WaybillsUpdateModel.

                - notes (str): notes of the WaybillsUpdateModel.

                - products (str): products of the WaybillsUpdateModel.

                - related_documents_notes (str): related_documents_notes of the WaybillsUpdateModel.

                - status (str): status of the WaybillsUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the WaybillsUpdateModel.

                - your_reference (str): your_reference of the WaybillsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
