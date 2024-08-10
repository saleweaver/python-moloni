from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class CountriesCountModifiedSinceModel(BaseModel):
    lastmodified: Optional[str] = None


class CountriesGetModifiedSinceModel(BaseModel):
    lastmodified: Optional[str] = None


class CountriesClient(MoloniBaseClient):

    @endpoint("/<version>/countries/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[CountriesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[CountriesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[CountriesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the CountriesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CountriesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/countries/getAll/", method="post")
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

    @endpoint("/<version>/countries/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[CountriesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[CountriesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[CountriesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the CountriesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CountriesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
