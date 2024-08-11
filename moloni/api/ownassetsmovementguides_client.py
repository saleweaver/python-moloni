from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = OwnassetsmovementguidesClient(*args, **kwargs)
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


class OwnassetsmovementguidesCountModel(ApiRequestModel):
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


class OwnassetsmovementguidesDeleteModel(ApiRequestModel):
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


class OwnassetsmovementguidesGetAllModel(ApiRequestModel):
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


class OwnassetsmovementguidesGetOneModel(ApiRequestModel):
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


class OwnassetsmovementguidesInsertModel(ApiRequestModel):
    company_id: Union[str, int]
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


class OwnassetsmovementguidesSetTransportCodeModel(ApiRequestModel):
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


class OwnassetsmovementguidesUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
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


class OwnassetsmovementguidesClient(MoloniBaseClient):

    @endpoint("/<version>/ownAssetsMovementGuides/count/", method="post")
    def count(self, data: Union[OwnassetsmovementguidesCountModel, dict], **kwargs):
        """
        count(self, data: Union[OwnassetsmovementguidesCountModel, dict], **kwargs)

        Args:

            data (Union[OwnassetsmovementguidesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the OwnassetsmovementguidesCountModel.

                - customer_id (Union[str, int]): customer_id of the OwnassetsmovementguidesCountModel.

                - date (str): date of the OwnassetsmovementguidesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the OwnassetsmovementguidesCountModel.

                - number (str): number of the OwnassetsmovementguidesCountModel.

                - year (str): year of the OwnassetsmovementguidesCountModel.

                - your_reference (str): your_reference of the OwnassetsmovementguidesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, OwnassetsmovementguidesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/ownAssetsMovementGuides/delete/", method="post")
    def delete(self, data: Union[OwnassetsmovementguidesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[OwnassetsmovementguidesDeleteModel, dict], **kwargs)

        Args:

            data (Union[OwnassetsmovementguidesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the OwnassetsmovementguidesDeleteModel.

                - document_id (Union[str, int]): document_id of the OwnassetsmovementguidesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, OwnassetsmovementguidesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/ownAssetsMovementGuides/getAll/", method="post")
    def get_all(self, data: Union[OwnassetsmovementguidesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[OwnassetsmovementguidesGetAllModel, dict], **kwargs)

        Args:

            data (Union[OwnassetsmovementguidesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the OwnassetsmovementguidesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the OwnassetsmovementguidesGetAllModel.

                - date (str): date of the OwnassetsmovementguidesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the OwnassetsmovementguidesGetAllModel.

                - number (str): number of the OwnassetsmovementguidesGetAllModel.

                - offset (str): offset of the OwnassetsmovementguidesGetAllModel.

                - qty (str): qty of the OwnassetsmovementguidesGetAllModel.

                - year (str): year of the OwnassetsmovementguidesGetAllModel.

                - your_reference (str): your_reference of the OwnassetsmovementguidesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, OwnassetsmovementguidesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/ownAssetsMovementGuides/getOne/", method="post")
    def get_one(self, data: Union[OwnassetsmovementguidesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[OwnassetsmovementguidesGetOneModel, dict], **kwargs)

        Args:

            data (Union[OwnassetsmovementguidesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the OwnassetsmovementguidesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the OwnassetsmovementguidesGetOneModel.

                - date (str): date of the OwnassetsmovementguidesGetOneModel.

                - document_id (Union[str, int]): document_id of the OwnassetsmovementguidesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the OwnassetsmovementguidesGetOneModel.

                - number (str): number of the OwnassetsmovementguidesGetOneModel.

                - year (str): year of the OwnassetsmovementguidesGetOneModel.

                - your_reference (str): your_reference of the OwnassetsmovementguidesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, OwnassetsmovementguidesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/ownAssetsMovementGuides/insert/", method="post")
    def insert(self, data: Union[OwnassetsmovementguidesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[OwnassetsmovementguidesInsertModel, dict], **kwargs)

        Args:

            data (Union[OwnassetsmovementguidesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the OwnassetsmovementguidesInsertModel.

                - customer_id (Union[str, int]): customer_id of the OwnassetsmovementguidesInsertModel.

                - date (str): date of the OwnassetsmovementguidesInsertModel.

                - delivery_datetime (str): delivery_datetime of the OwnassetsmovementguidesInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the OwnassetsmovementguidesInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the OwnassetsmovementguidesInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the OwnassetsmovementguidesInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the OwnassetsmovementguidesInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the OwnassetsmovementguidesInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the OwnassetsmovementguidesInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the OwnassetsmovementguidesInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the OwnassetsmovementguidesInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the OwnassetsmovementguidesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the OwnassetsmovementguidesInsertModel.

                - notes (str): notes of the OwnassetsmovementguidesInsertModel.

                - products (str): products of the OwnassetsmovementguidesInsertModel.

                - status (str): status of the OwnassetsmovementguidesInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the OwnassetsmovementguidesInsertModel.

                - your_reference (str): your_reference of the OwnassetsmovementguidesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, OwnassetsmovementguidesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/ownAssetsMovementGuides/setTransportCode/", method="post")
    def set_transport_code(
        self, data: Union[OwnassetsmovementguidesSetTransportCodeModel, dict], **kwargs
    ):
        """
        set_transport_code(self, data: Union[OwnassetsmovementguidesSetTransportCodeModel, dict], **kwargs)

        Args:

            data (Union[OwnassetsmovementguidesSetTransportCodeModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the OwnassetsmovementguidesSetTransportCodeModel.

                - document_id (Union[str, int]): document_id of the OwnassetsmovementguidesSetTransportCodeModel.

                - transport_code (str): transport_code of the OwnassetsmovementguidesSetTransportCodeModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, OwnassetsmovementguidesSetTransportCodeModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/ownAssetsMovementGuides/update/", method="post")
    def update(self, data: Union[OwnassetsmovementguidesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[OwnassetsmovementguidesUpdateModel, dict], **kwargs)

        Args:

            data (Union[OwnassetsmovementguidesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the OwnassetsmovementguidesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the OwnassetsmovementguidesUpdateModel.

                - date (str): date of the OwnassetsmovementguidesUpdateModel.

                - delivery_datetime (str): delivery_datetime of the OwnassetsmovementguidesUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the OwnassetsmovementguidesUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the OwnassetsmovementguidesUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the OwnassetsmovementguidesUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the OwnassetsmovementguidesUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the OwnassetsmovementguidesUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the OwnassetsmovementguidesUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the OwnassetsmovementguidesUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the OwnassetsmovementguidesUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the OwnassetsmovementguidesUpdateModel.

                - document_id (Union[str, int]): document_id of the OwnassetsmovementguidesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the OwnassetsmovementguidesUpdateModel.

                - notes (str): notes of the OwnassetsmovementguidesUpdateModel.

                - products (str): products of the OwnassetsmovementguidesUpdateModel.

                - status (str): status of the OwnassetsmovementguidesUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the OwnassetsmovementguidesUpdateModel.

                - your_reference (str): your_reference of the OwnassetsmovementguidesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, OwnassetsmovementguidesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
