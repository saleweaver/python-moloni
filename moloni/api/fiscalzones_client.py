from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class FiscalzonesCountModifiedSinceModel(BaseModel):
    lastmodified: Optional[str] = None


class FiscalzonesGetAllModel(BaseModel):
    country_id: Optional[Union[str, int]] = None


class FiscalzonesGetModifiedSinceModel(BaseModel):
    lastmodified: Optional[str] = None


class FiscalzonesClient(MoloniBaseClient):

    @endpoint("/<version>/fiscalZones/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[FiscalzonesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[FiscalzonesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[FiscalzonesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the FiscalzonesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, FiscalzonesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/fiscalZones/getAll/", method="post")
    def get_all(self, data: Union[FiscalzonesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[FiscalzonesGetAllModel, dict], **kwargs)

        Args:

            data (Union[FiscalzonesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - country_id (Union[str, int]): country_id of the FiscalzonesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, FiscalzonesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/fiscalZones/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[FiscalzonesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[FiscalzonesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[FiscalzonesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the FiscalzonesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, FiscalzonesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
