from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class TaxexemptionsCountModifiedSinceModel(BaseModel):
    lastmodified: Optional[str] = None


class TaxexemptionsGetModifiedSinceModel(BaseModel):
    lastmodified: Optional[str] = None


class TaxexemptionsClient(MoloniBaseClient):

    @endpoint("/<version>/taxExemptions/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[TaxexemptionsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[TaxexemptionsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[TaxexemptionsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the TaxexemptionsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, TaxexemptionsCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/taxExemptions/getAll/", method="post")
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

    @endpoint("/<version>/taxExemptions/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[TaxexemptionsGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[TaxexemptionsGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[TaxexemptionsGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the TaxexemptionsGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, TaxexemptionsGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
