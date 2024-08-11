from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = DocumentmodelsClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class DocumentmodelsCountModifiedSinceModel(ApiRequestModel):
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.count_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DocumentmodelsGetModifiedSinceModel(ApiRequestModel):
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


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
