from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class DeductionsCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class DeductionsDeleteModel(BaseModel):
    company_id: Union[str, int]
    deduction_id: Union[str, int]


class DeductionsGetAllModel(BaseModel):
    company_id: Union[str, int]


class DeductionsGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class DeductionsInsertModel(BaseModel):
    company_id: Union[str, int]
    name: str
    value: str


class DeductionsUpdateModel(BaseModel):
    company_id: Union[str, int]
    deduction_id: Union[str, int]
    name: str = None
    value: str = None


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
