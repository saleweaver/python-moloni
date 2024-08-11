from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = SalesmenClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class SalesmenCountModifiedSinceModel(ApiRequestModel):
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


class SalesmenDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    salesman_id: Optional[Union[str, int]] = None

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


class SalesmenGetAllModel(ApiRequestModel):
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


class SalesmenGetModifiedSinceModel(ApiRequestModel):
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


class SalesmenGetOneModel(ApiRequestModel):
    company_id: Union[str, int]
    salesman_id: Optional[Union[str, int]] = None

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


class SalesmenInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    base_commission: Optional[str] = None
    city: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    language_id: Optional[Union[str, int]] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    number: Optional[str] = None
    phone: Optional[str] = None
    qty_copies_document: Optional[str] = None
    vat: Optional[str] = None
    website: Optional[str] = None
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


class SalesmenUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    base_commission: Optional[str] = None
    city: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    language_id: Optional[Union[str, int]] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    number: Optional[str] = None
    phone: Optional[str] = None
    qty_copies_document: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    vat: Optional[str] = None
    website: Optional[str] = None
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


class SalesmenClient(MoloniBaseClient):

    @endpoint("/<version>/salesmen/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[SalesmenCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[SalesmenCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[SalesmenCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the SalesmenCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/delete/", method="post")
    def delete(self, data: Union[SalesmenDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[SalesmenDeleteModel, dict], **kwargs)

        Args:

            data (Union[SalesmenDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenDeleteModel.

                - salesman_id (Union[str, int]): salesman_id of the SalesmenDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/getAll/", method="post")
    def get_all(self, data: Union[SalesmenGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[SalesmenGetAllModel, dict], **kwargs)

        Args:

            data (Union[SalesmenGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[SalesmenGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[SalesmenGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[SalesmenGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the SalesmenGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/getOne/", method="post")
    def get_one(self, data: Union[SalesmenGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[SalesmenGetOneModel, dict], **kwargs)

        Args:

            data (Union[SalesmenGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the SalesmenGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/insert/", method="post")
    def insert(self, data: Union[SalesmenInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[SalesmenInsertModel, dict], **kwargs)

        Args:

            data (Union[SalesmenInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the SalesmenInsertModel.

                - base_commission (str): base_commission of the SalesmenInsertModel.

                - city (str): city of the SalesmenInsertModel.

                - company_id (Union[str, int]): company_id of the SalesmenInsertModel.

                - country_id (Union[str, int]): country_id of the SalesmenInsertModel.

                - email (str): email of the SalesmenInsertModel.

                - fax (str): fax of the SalesmenInsertModel.

                - language_id (Union[str, int]): language_id of the SalesmenInsertModel.

                - name (str): name of the SalesmenInsertModel.

                - notes (str): notes of the SalesmenInsertModel.

                - number (str): number of the SalesmenInsertModel.

                - phone (str): phone of the SalesmenInsertModel.

                - qty_copies_document (str): qty_copies_document of the SalesmenInsertModel.

                - vat (str): vat of the SalesmenInsertModel.

                - website (str): website of the SalesmenInsertModel.

                - zip_code (str): zip_code of the SalesmenInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/update/", method="post")
    def update(self, data: Union[SalesmenUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[SalesmenUpdateModel, dict], **kwargs)

        Args:

            data (Union[SalesmenUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the SalesmenUpdateModel.

                - base_commission (str): base_commission of the SalesmenUpdateModel.

                - city (str): city of the SalesmenUpdateModel.

                - company_id (Union[str, int]): company_id of the SalesmenUpdateModel.

                - country_id (Union[str, int]): country_id of the SalesmenUpdateModel.

                - email (str): email of the SalesmenUpdateModel.

                - fax (str): fax of the SalesmenUpdateModel.

                - language_id (Union[str, int]): language_id of the SalesmenUpdateModel.

                - name (str): name of the SalesmenUpdateModel.

                - notes (str): notes of the SalesmenUpdateModel.

                - number (str): number of the SalesmenUpdateModel.

                - phone (str): phone of the SalesmenUpdateModel.

                - qty_copies_document (str): qty_copies_document of the SalesmenUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the SalesmenUpdateModel.

                - vat (str): vat of the SalesmenUpdateModel.

                - website (str): website of the SalesmenUpdateModel.

                - zip_code (str): zip_code of the SalesmenUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
