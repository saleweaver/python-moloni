from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = DeliverynotesClient(*args, **kwargs)
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


class DeliverynotesCountModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
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


class DeliverynotesDeleteModel(ApiRequestModel):
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


class DeliverynotesGetAllModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
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


class DeliverynotesGetOneModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
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


class DeliverynotesInsertModel(ApiRequestModel):
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
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
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


class DeliverynotesSetTransportCodeModel(ApiRequestModel):
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


class DeliverynotesUpdateModel(ApiRequestModel):
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
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
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


class DeliverynotesClient(MoloniBaseClient):

    @endpoint("/<version>/deliveryNotes/count/", method="post")
    def count(self, data: Union[DeliverynotesCountModel, dict], **kwargs):
        """
        count(self, data: Union[DeliverynotesCountModel, dict], **kwargs)

        Args:

            data (Union[DeliverynotesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverynotesCountModel.

                - customer_id (Union[str, int]): customer_id of the DeliverynotesCountModel.

                - date (str): date of the DeliverynotesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the DeliverynotesCountModel.

                - number (str): number of the DeliverynotesCountModel.

                - salesman_id (Union[str, int]): salesman_id of the DeliverynotesCountModel.

                - year (str): year of the DeliverynotesCountModel.

                - your_reference (str): your_reference of the DeliverynotesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverynotesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryNotes/delete/", method="post")
    def delete(self, data: Union[DeliverynotesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[DeliverynotesDeleteModel, dict], **kwargs)

        Args:

            data (Union[DeliverynotesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverynotesDeleteModel.

                - document_id (Union[str, int]): document_id of the DeliverynotesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverynotesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryNotes/getAll/", method="post")
    def get_all(self, data: Union[DeliverynotesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[DeliverynotesGetAllModel, dict], **kwargs)

        Args:

            data (Union[DeliverynotesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverynotesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the DeliverynotesGetAllModel.

                - date (str): date of the DeliverynotesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the DeliverynotesGetAllModel.

                - number (str): number of the DeliverynotesGetAllModel.

                - offset (str): offset of the DeliverynotesGetAllModel.

                - qty (str): qty of the DeliverynotesGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the DeliverynotesGetAllModel.

                - year (str): year of the DeliverynotesGetAllModel.

                - your_reference (str): your_reference of the DeliverynotesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverynotesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryNotes/getOne/", method="post")
    def get_one(self, data: Union[DeliverynotesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[DeliverynotesGetOneModel, dict], **kwargs)

        Args:

            data (Union[DeliverynotesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverynotesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the DeliverynotesGetOneModel.

                - date (str): date of the DeliverynotesGetOneModel.

                - document_id (Union[str, int]): document_id of the DeliverynotesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the DeliverynotesGetOneModel.

                - number (str): number of the DeliverynotesGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the DeliverynotesGetOneModel.

                - year (str): year of the DeliverynotesGetOneModel.

                - your_reference (str): your_reference of the DeliverynotesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverynotesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryNotes/insert/", method="post")
    def insert(self, data: Union[DeliverynotesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[DeliverynotesInsertModel, dict], **kwargs)

        Args:

            data (Union[DeliverynotesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the DeliverynotesInsertModel.

                - company_id (Union[str, int]): company_id of the DeliverynotesInsertModel.

                - customer_id (Union[str, int]): customer_id of the DeliverynotesInsertModel.

                - date (str): date of the DeliverynotesInsertModel.

                - delivery_datetime (str): delivery_datetime of the DeliverynotesInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the DeliverynotesInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the DeliverynotesInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the DeliverynotesInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the DeliverynotesInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the DeliverynotesInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the DeliverynotesInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the DeliverynotesInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the DeliverynotesInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the DeliverynotesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the DeliverynotesInsertModel.

                - notes (str): notes of the DeliverynotesInsertModel.

                - products (str): products of the DeliverynotesInsertModel.

                - related_documents_notes (str): related_documents_notes of the DeliverynotesInsertModel.

                - salesman_commission (str): salesman_commission of the DeliverynotesInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the DeliverynotesInsertModel.

                - status (str): status of the DeliverynotesInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the DeliverynotesInsertModel.

                - your_reference (str): your_reference of the DeliverynotesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverynotesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryNotes/setTransportCode/", method="post")
    def set_transport_code(
        self, data: Union[DeliverynotesSetTransportCodeModel, dict], **kwargs
    ):
        """
        set_transport_code(self, data: Union[DeliverynotesSetTransportCodeModel, dict], **kwargs)

        Args:

            data (Union[DeliverynotesSetTransportCodeModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverynotesSetTransportCodeModel.

                - document_id (Union[str, int]): document_id of the DeliverynotesSetTransportCodeModel.

                - transport_code (str): transport_code of the DeliverynotesSetTransportCodeModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverynotesSetTransportCodeModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryNotes/update/", method="post")
    def update(self, data: Union[DeliverynotesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[DeliverynotesUpdateModel, dict], **kwargs)

        Args:

            data (Union[DeliverynotesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the DeliverynotesUpdateModel.

                - company_id (Union[str, int]): company_id of the DeliverynotesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the DeliverynotesUpdateModel.

                - date (str): date of the DeliverynotesUpdateModel.

                - delivery_datetime (str): delivery_datetime of the DeliverynotesUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the DeliverynotesUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the DeliverynotesUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the DeliverynotesUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the DeliverynotesUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the DeliverynotesUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the DeliverynotesUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the DeliverynotesUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the DeliverynotesUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the DeliverynotesUpdateModel.

                - document_id (Union[str, int]): document_id of the DeliverynotesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the DeliverynotesUpdateModel.

                - notes (str): notes of the DeliverynotesUpdateModel.

                - products (str): products of the DeliverynotesUpdateModel.

                - related_documents_notes (str): related_documents_notes of the DeliverynotesUpdateModel.

                - salesman_commission (str): salesman_commission of the DeliverynotesUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the DeliverynotesUpdateModel.

                - status (str): status of the DeliverynotesUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the DeliverynotesUpdateModel.

                - your_reference (str): your_reference of the DeliverynotesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverynotesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
