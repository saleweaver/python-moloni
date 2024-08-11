from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = IdentificationtemplatesClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class IdentificationtemplatesCountModifiedSinceModel(ApiRequestModel):
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


class IdentificationtemplatesDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    template_id: Optional[Union[str, int]] = None

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


class IdentificationtemplatesGetAllModel(ApiRequestModel):
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


class IdentificationtemplatesGetModifiedSinceModel(ApiRequestModel):
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


class IdentificationtemplatesInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    business_name: Optional[str] = None
    city: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    documents_footnote: Optional[str] = None
    email: Optional[str] = None
    email_sender_address: Optional[str] = None
    email_sender_name: Optional[str] = None
    fax: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    phone: Optional[str] = None
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


class IdentificationtemplatesUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    business_name: Optional[str] = None
    city: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    documents_footnote: Optional[str] = None
    email: Optional[str] = None
    email_sender_address: Optional[str] = None
    email_sender_name: Optional[str] = None
    fax: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    phone: Optional[str] = None
    template_id: Optional[Union[str, int]] = None
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


class IdentificationtemplatesClient(MoloniBaseClient):

    @endpoint("/<version>/identificationTemplates/countModifiedSince/", method="post")
    def count_modified_since(
        self,
        data: Union[IdentificationtemplatesCountModifiedSinceModel, dict],
        **kwargs
    ):
        """
        count_modified_since(self, data: Union[IdentificationtemplatesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the IdentificationtemplatesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, IdentificationtemplatesCountModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/delete/", method="post")
    def delete(self, data: Union[IdentificationtemplatesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[IdentificationtemplatesDeleteModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesDeleteModel.

                - template_id (Union[str, int]): template_id of the IdentificationtemplatesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, IdentificationtemplatesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/getAll/", method="post")
    def get_all(self, data: Union[IdentificationtemplatesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[IdentificationtemplatesGetAllModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, IdentificationtemplatesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[IdentificationtemplatesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[IdentificationtemplatesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the IdentificationtemplatesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, IdentificationtemplatesGetModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/insert/", method="post")
    def insert(self, data: Union[IdentificationtemplatesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[IdentificationtemplatesInsertModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the IdentificationtemplatesInsertModel.

                - business_name (str): business_name of the IdentificationtemplatesInsertModel.

                - city (str): city of the IdentificationtemplatesInsertModel.

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesInsertModel.

                - country_id (Union[str, int]): country_id of the IdentificationtemplatesInsertModel.

                - documents_footnote (str): documents_footnote of the IdentificationtemplatesInsertModel.

                - email (str): email of the IdentificationtemplatesInsertModel.

                - email_sender_address (str): email_sender_address of the IdentificationtemplatesInsertModel.

                - email_sender_name (str): email_sender_name of the IdentificationtemplatesInsertModel.

                - fax (str): fax of the IdentificationtemplatesInsertModel.

                - name (str): name of the IdentificationtemplatesInsertModel.

                - notes (str): notes of the IdentificationtemplatesInsertModel.

                - phone (str): phone of the IdentificationtemplatesInsertModel.

                - website (str): website of the IdentificationtemplatesInsertModel.

                - zip_code (str): zip_code of the IdentificationtemplatesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, IdentificationtemplatesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/update/", method="post")
    def update(self, data: Union[IdentificationtemplatesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[IdentificationtemplatesUpdateModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the IdentificationtemplatesUpdateModel.

                - business_name (str): business_name of the IdentificationtemplatesUpdateModel.

                - city (str): city of the IdentificationtemplatesUpdateModel.

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesUpdateModel.

                - country_id (Union[str, int]): country_id of the IdentificationtemplatesUpdateModel.

                - documents_footnote (str): documents_footnote of the IdentificationtemplatesUpdateModel.

                - email (str): email of the IdentificationtemplatesUpdateModel.

                - email_sender_address (str): email_sender_address of the IdentificationtemplatesUpdateModel.

                - email_sender_name (str): email_sender_name of the IdentificationtemplatesUpdateModel.

                - fax (str): fax of the IdentificationtemplatesUpdateModel.

                - name (str): name of the IdentificationtemplatesUpdateModel.

                - notes (str): notes of the IdentificationtemplatesUpdateModel.

                - phone (str): phone of the IdentificationtemplatesUpdateModel.

                - template_id (Union[str, int]): template_id of the IdentificationtemplatesUpdateModel.

                - website (str): website of the IdentificationtemplatesUpdateModel.

                - zip_code (str): zip_code of the IdentificationtemplatesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, IdentificationtemplatesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
