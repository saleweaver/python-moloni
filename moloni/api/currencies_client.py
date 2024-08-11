from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = CurrenciesClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class CurrenciesCountModifiedSinceModel(ApiRequestModel):
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


class CurrenciesGetModifiedSinceModel(ApiRequestModel):
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


class CurrenciesClient(MoloniBaseClient):

    @endpoint("/<version>/currencies/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[CurrenciesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[CurrenciesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[CurrenciesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the CurrenciesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CurrenciesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/currencies/getAll/", method="post")
    def get_all(self, **kwargs):
        """
        get_all(self, **kwargs)

        Args:


        Returns:
            ApiResponse: The response from the API.
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**kwargs}
        )

    @endpoint("/<version>/currencies/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[CurrenciesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[CurrenciesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[CurrenciesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the CurrenciesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CurrenciesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
