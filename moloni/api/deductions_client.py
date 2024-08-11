from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = DeductionsClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class DeductionsCountModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.count_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DeductionsDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    deduction_id: Optional[Union[str, int]] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.delete(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DeductionsGetAllModel(ApiRequestModel):
    company_id: Union[str, int]

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_all(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DeductionsGetModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DeductionsInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    name: Optional[str] = None
    value: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.insert(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DeductionsUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    deduction_id: Optional[Union[str, int]] = None
    name: Optional[str] = None
    value: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.update(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DeductionsClient(MoloniBaseClient):

    @endpoint("/<version>/deductions/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[DeductionsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[DeductionsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[DeductionsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeductionsCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the DeductionsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeductionsCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deductions/delete/", method="post")
    def delete(self, data: Union[DeductionsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[DeductionsDeleteModel, dict], **kwargs)

        Args:

            data (Union[DeductionsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeductionsDeleteModel.

                - deduction_id (Union[str, int]): deduction_id of the DeductionsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeductionsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deductions/getAll/", method="post")
    def get_all(self, data: Union[DeductionsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[DeductionsGetAllModel, dict], **kwargs)

        Args:

            data (Union[DeductionsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeductionsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeductionsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deductions/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[DeductionsGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[DeductionsGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[DeductionsGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeductionsGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the DeductionsGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeductionsGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deductions/insert/", method="post")
    def insert(self, data: Union[DeductionsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[DeductionsInsertModel, dict], **kwargs)

        Args:

            data (Union[DeductionsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeductionsInsertModel.

                - name (str): name of the DeductionsInsertModel.

                - value (str): value of the DeductionsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeductionsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deductions/update/", method="post")
    def update(self, data: Union[DeductionsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[DeductionsUpdateModel, dict], **kwargs)

        Args:

            data (Union[DeductionsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeductionsUpdateModel.

                - deduction_id (Union[str, int]): deduction_id of the DeductionsUpdateModel.

                - name (str): name of the DeductionsUpdateModel.

                - value (str): value of the DeductionsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeductionsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
