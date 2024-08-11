from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = CurrenciesClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class CurrenciesCountModifiedSinceModel(ApiRequestModel):
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.count_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class CurrenciesGetModifiedSinceModel(ApiRequestModel):
    lastmodified: Optional[str] = None

    def request(self):
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
