from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = BillsofladingClient(*args, **kwargs)
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


class BillsofladingCountModel(ApiRequestModel):
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


class BillsofladingDeleteModel(ApiRequestModel):
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


class BillsofladingGetAllModel(ApiRequestModel):
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


class BillsofladingGetOneModel(ApiRequestModel):
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


class BillsofladingInsertModel(ApiRequestModel):
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


class BillsofladingSetTransportCodeModel(ApiRequestModel):
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


class BillsofladingUpdateModel(ApiRequestModel):
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


class BillsofladingClient(MoloniBaseClient):

    @endpoint("/<version>/billsOfLading/count/", method="post")
    def count(self, data: Union[BillsofladingCountModel, dict], **kwargs):
        """
        count(self, data: Union[BillsofladingCountModel, dict], **kwargs)

        Args:

            data (Union[BillsofladingCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the BillsofladingCountModel.

                - customer_id (Union[str, int]): customer_id of the BillsofladingCountModel.

                - date (str): date of the BillsofladingCountModel.

                - document_set_id (Union[str, int]): document_set_id of the BillsofladingCountModel.

                - number (str): number of the BillsofladingCountModel.

                - year (str): year of the BillsofladingCountModel.

                - your_reference (str): your_reference of the BillsofladingCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BillsofladingCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/billsOfLading/delete/", method="post")
    def delete(self, data: Union[BillsofladingDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[BillsofladingDeleteModel, dict], **kwargs)

        Args:

            data (Union[BillsofladingDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the BillsofladingDeleteModel.

                - document_id (Union[str, int]): document_id of the BillsofladingDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BillsofladingDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/billsOfLading/getAll/", method="post")
    def get_all(self, data: Union[BillsofladingGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[BillsofladingGetAllModel, dict], **kwargs)

        Args:

            data (Union[BillsofladingGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the BillsofladingGetAllModel.

                - customer_id (Union[str, int]): customer_id of the BillsofladingGetAllModel.

                - date (str): date of the BillsofladingGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the BillsofladingGetAllModel.

                - number (str): number of the BillsofladingGetAllModel.

                - offset (str): offset of the BillsofladingGetAllModel.

                - qty (str): qty of the BillsofladingGetAllModel.

                - year (str): year of the BillsofladingGetAllModel.

                - your_reference (str): your_reference of the BillsofladingGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BillsofladingGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/billsOfLading/getOne/", method="post")
    def get_one(self, data: Union[BillsofladingGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[BillsofladingGetOneModel, dict], **kwargs)

        Args:

            data (Union[BillsofladingGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the BillsofladingGetOneModel.

                - customer_id (Union[str, int]): customer_id of the BillsofladingGetOneModel.

                - date (str): date of the BillsofladingGetOneModel.

                - document_id (Union[str, int]): document_id of the BillsofladingGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the BillsofladingGetOneModel.

                - number (str): number of the BillsofladingGetOneModel.

                - year (str): year of the BillsofladingGetOneModel.

                - your_reference (str): your_reference of the BillsofladingGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BillsofladingGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/billsOfLading/insert/", method="post")
    def insert(self, data: Union[BillsofladingInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[BillsofladingInsertModel, dict], **kwargs)

        Args:

            data (Union[BillsofladingInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the BillsofladingInsertModel.

                - company_id (Union[str, int]): company_id of the BillsofladingInsertModel.

                - customer_id (Union[str, int]): customer_id of the BillsofladingInsertModel.

                - date (str): date of the BillsofladingInsertModel.

                - delivery_datetime (str): delivery_datetime of the BillsofladingInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the BillsofladingInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the BillsofladingInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the BillsofladingInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the BillsofladingInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the BillsofladingInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the BillsofladingInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the BillsofladingInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the BillsofladingInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the BillsofladingInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the BillsofladingInsertModel.

                - notes (str): notes of the BillsofladingInsertModel.

                - products (str): products of the BillsofladingInsertModel.

                - related_documents_notes (str): related_documents_notes of the BillsofladingInsertModel.

                - status (str): status of the BillsofladingInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the BillsofladingInsertModel.

                - your_reference (str): your_reference of the BillsofladingInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BillsofladingInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/billsOfLading/setTransportCode/", method="post")
    def set_transport_code(
        self, data: Union[BillsofladingSetTransportCodeModel, dict], **kwargs
    ):
        """
        set_transport_code(self, data: Union[BillsofladingSetTransportCodeModel, dict], **kwargs)

        Args:

            data (Union[BillsofladingSetTransportCodeModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the BillsofladingSetTransportCodeModel.

                - document_id (Union[str, int]): document_id of the BillsofladingSetTransportCodeModel.

                - transport_code (str): transport_code of the BillsofladingSetTransportCodeModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BillsofladingSetTransportCodeModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/billsOfLading/update/", method="post")
    def update(self, data: Union[BillsofladingUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[BillsofladingUpdateModel, dict], **kwargs)

        Args:

            data (Union[BillsofladingUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the BillsofladingUpdateModel.

                - company_id (Union[str, int]): company_id of the BillsofladingUpdateModel.

                - customer_id (Union[str, int]): customer_id of the BillsofladingUpdateModel.

                - date (str): date of the BillsofladingUpdateModel.

                - delivery_datetime (str): delivery_datetime of the BillsofladingUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the BillsofladingUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the BillsofladingUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the BillsofladingUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the BillsofladingUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the BillsofladingUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the BillsofladingUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the BillsofladingUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the BillsofladingUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the BillsofladingUpdateModel.

                - document_id (Union[str, int]): document_id of the BillsofladingUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the BillsofladingUpdateModel.

                - notes (str): notes of the BillsofladingUpdateModel.

                - products (str): products of the BillsofladingUpdateModel.

                - related_documents_notes (str): related_documents_notes of the BillsofladingUpdateModel.

                - status (str): status of the BillsofladingUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the BillsofladingUpdateModel.

                - your_reference (str): your_reference of the BillsofladingUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BillsofladingUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
