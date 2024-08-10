from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class LanguagesCountModifiedSinceModel(BaseModel):
    lastmodified: str


class LanguagesGetModifiedSinceModel(BaseModel):
    lastmodified: str


class LanguagesClient(MoloniBaseClient):

    @endpoint("/<version>/languages/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[LanguagesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[LanguagesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[LanguagesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the LanguagesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, LanguagesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/languages/getAll/", method="post")
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

    @endpoint("/<version>/languages/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[LanguagesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[LanguagesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[LanguagesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the LanguagesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, LanguagesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
