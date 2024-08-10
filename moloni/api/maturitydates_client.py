from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class MaturitydatesCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None


class MaturitydatesDeleteModel(BaseModel):
    company_id: Union[str, int]
    maturity_date_id: Optional[Union[str, int]] = None


class MaturitydatesGetAllModel(BaseModel):
    company_id: Union[str, int]


class MaturitydatesGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None


class MaturitydatesInsertModel(BaseModel):
    company_id: Union[str, int]
    associated_discount: Optional[str] = None
    days: Optional[str] = None
    name: Optional[str] = None


class MaturitydatesUpdateModel(BaseModel):
    company_id: Union[str, int]
    associated_discount: Optional[str] = None
    days: Optional[str] = None
    maturity_date_id: Optional[Union[str, int]] = None
    name: Optional[str] = None


class MaturitydatesClient(MoloniBaseClient):

    @endpoint("/<version>/maturityDates/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[MaturitydatesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[MaturitydatesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[MaturitydatesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MaturitydatesCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the MaturitydatesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MaturitydatesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/maturityDates/delete/", method="post")
    def delete(self, data: Union[MaturitydatesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[MaturitydatesDeleteModel, dict], **kwargs)

        Args:

            data (Union[MaturitydatesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MaturitydatesDeleteModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the MaturitydatesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MaturitydatesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/maturityDates/getAll/", method="post")
    def get_all(self, data: Union[MaturitydatesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[MaturitydatesGetAllModel, dict], **kwargs)

        Args:

            data (Union[MaturitydatesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MaturitydatesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MaturitydatesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/maturityDates/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[MaturitydatesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[MaturitydatesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[MaturitydatesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MaturitydatesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the MaturitydatesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MaturitydatesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/maturityDates/insert/", method="post")
    def insert(self, data: Union[MaturitydatesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[MaturitydatesInsertModel, dict], **kwargs)

        Args:

            data (Union[MaturitydatesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_discount (str): associated_discount of the MaturitydatesInsertModel.

                - company_id (Union[str, int]): company_id of the MaturitydatesInsertModel.

                - days (str): days of the MaturitydatesInsertModel.

                - name (str): name of the MaturitydatesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MaturitydatesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/maturityDates/update/", method="post")
    def update(self, data: Union[MaturitydatesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[MaturitydatesUpdateModel, dict], **kwargs)

        Args:

            data (Union[MaturitydatesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_discount (str): associated_discount of the MaturitydatesUpdateModel.

                - company_id (Union[str, int]): company_id of the MaturitydatesUpdateModel.

                - days (str): days of the MaturitydatesUpdateModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the MaturitydatesUpdateModel.

                - name (str): name of the MaturitydatesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MaturitydatesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
