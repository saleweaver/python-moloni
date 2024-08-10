from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class CurrenciesCountModifiedSinceModel(BaseModel):
    lastmodified: Optional[str] = None


class CurrenciesGetModifiedSinceModel(BaseModel):
    lastmodified: Optional[str] = None


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
