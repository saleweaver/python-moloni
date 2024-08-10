from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class DocumentmodelsCountModifiedSinceModel(BaseModel):
    lastmodified: str


class DocumentmodelsGetModifiedSinceModel(BaseModel):
    lastmodified: str


class DocumentmodelsClient(MoloniBaseClient):

    @endpoint("/<version>/documentModels/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[DocumentmodelsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[DocumentmodelsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[DocumentmodelsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the DocumentmodelsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentmodelsCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documentModels/getAll/", method="post")
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

    @endpoint("/<version>/documentModels/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[DocumentmodelsGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[DocumentmodelsGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[DocumentmodelsGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - lastmodified (str): lastmodified of the DocumentmodelsGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentmodelsGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
