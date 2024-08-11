from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = WarehousesClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class Suppliers(BaseModel):
    cost_price: Optional[Any] = None
    supplier_id: Optional[Any] = None


class Taxes(BaseModel):
    cumulative: Optional[Any] = None
    order: Optional[Any] = None
    tax_id: Optional[Any] = None
    value: Optional[Any] = None


class Warehouses(BaseModel):
    stock: Optional[Any] = None
    warehouse_id: Optional[Any] = None


class WarehousesCountModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

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
            response = self._api_client.count_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class WarehousesDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    warehouse_id: Optional[Union[str, int]] = None

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


class WarehousesGetAllModel(ApiRequestModel):
    company_id: Union[str, int]

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


class WarehousesGetModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

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
            response = self._api_client.get_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class WarehousesInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    city: Optional[str] = None
    code: Optional[str] = None
    contact_email: Optional[str] = None
    contact_name: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    fax: Optional[str] = None
    is_default: Optional[bool] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    zip_code: Optional[str] = None

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


class WarehousesUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    city: Optional[str] = None
    code: Optional[str] = None
    contact_email: Optional[str] = None
    contact_name: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    fax: Optional[str] = None
    is_default: Optional[bool] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    warehouse_id: Optional[Union[str, int]] = None
    zip_code: Optional[str] = None

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


class WarehousesClient(MoloniBaseClient):

    @endpoint("/<version>/warehouses/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[WarehousesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[WarehousesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[WarehousesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WarehousesCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the WarehousesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/delete/", method="post")
    def delete(self, data: Union[WarehousesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[WarehousesDeleteModel, dict], **kwargs)

        Args:

            data (Union[WarehousesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WarehousesDeleteModel.

                - warehouse_id (Union[str, int]): warehouse_id of the WarehousesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/getAll/", method="post")
    def get_all(self, data: Union[WarehousesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[WarehousesGetAllModel, dict], **kwargs)

        Args:

            data (Union[WarehousesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WarehousesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[WarehousesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[WarehousesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[WarehousesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WarehousesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the WarehousesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/insert/", method="post")
    def insert(self, data: Union[WarehousesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[WarehousesInsertModel, dict], **kwargs)

        Args:

            data (Union[WarehousesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the WarehousesInsertModel.

                - city (str): city of the WarehousesInsertModel.

                - code (str): code of the WarehousesInsertModel.

                - company_id (Union[str, int]): company_id of the WarehousesInsertModel.

                - contact_email (str): contact_email of the WarehousesInsertModel.

                - contact_name (str): contact_name of the WarehousesInsertModel.

                - country_id (Union[str, int]): country_id of the WarehousesInsertModel.

                - fax (str): fax of the WarehousesInsertModel.

                - is_default (bool): is_default of the WarehousesInsertModel.

                - phone (str): phone of the WarehousesInsertModel.

                - title (str): title of the WarehousesInsertModel.

                - zip_code (str): zip_code of the WarehousesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/update/", method="post")
    def update(self, data: Union[WarehousesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[WarehousesUpdateModel, dict], **kwargs)

        Args:

            data (Union[WarehousesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the WarehousesUpdateModel.

                - city (str): city of the WarehousesUpdateModel.

                - code (str): code of the WarehousesUpdateModel.

                - company_id (Union[str, int]): company_id of the WarehousesUpdateModel.

                - contact_email (str): contact_email of the WarehousesUpdateModel.

                - contact_name (str): contact_name of the WarehousesUpdateModel.

                - country_id (Union[str, int]): country_id of the WarehousesUpdateModel.

                - fax (str): fax of the WarehousesUpdateModel.

                - is_default (bool): is_default of the WarehousesUpdateModel.

                - phone (str): phone of the WarehousesUpdateModel.

                - title (str): title of the WarehousesUpdateModel.

                - warehouse_id (Union[str, int]): warehouse_id of the WarehousesUpdateModel.

                - zip_code (str): zip_code of the WarehousesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
