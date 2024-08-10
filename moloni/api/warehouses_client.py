from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class WarehousesCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class WarehousesDeleteModel(BaseModel):
    company_id: Union[str, int]
    warehouse_id: Union[str, int]


class WarehousesGetAllModel(BaseModel):
    company_id: Union[str, int]


class WarehousesGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class WarehousesInsertModel(BaseModel):
    address: str
    city: str
    code: str
    company_id: Union[str, int]
    contact_email: str
    contact_name: str
    country_id: Union[str, int]
    fax: str
    is_default: bool
    phone: str
    title: str
    zip_code: str


class WarehousesUpdateModel(BaseModel):
    company_id: Union[str, int]
    warehouse_id: Union[str, int]
    address: str = None
    city: str = None
    code: str = None
    contact_email: str = None
    contact_name: str = None
    country_id: Union[str, int] = None
    fax: str = None
    is_default: bool = None
    phone: str = None
    title: str = None
    zip_code: str = None


class WarehousesClient(MoloniBaseClient):

    @endpoint("/<version>/warehouses/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[WarehousesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[WarehousesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[WarehousesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WarehousesCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the WarehousesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/delete/", method="post")
    def delete(self, data: Union[WarehousesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[WarehousesDeleteModel, dict], **kwargs)

        Args:

            data (Union[WarehousesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WarehousesDeleteModel.

                - warehouse_id (Union[str, int]): warehouse_id of the WarehousesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/getAll/", method="post")
    def get_all(self, data: Union[WarehousesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[WarehousesGetAllModel, dict], **kwargs)

        Args:

            data (Union[WarehousesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WarehousesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[WarehousesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[WarehousesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[WarehousesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WarehousesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the WarehousesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/insert/", method="post")
    def insert(self, data: Union[WarehousesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[WarehousesInsertModel, dict], **kwargs)

        Args:

            data (Union[WarehousesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the WarehousesInsertModel.

                - city (str): city of the WarehousesInsertModel.

                - code (str): code of the WarehousesInsertModel.

                - company_id (Union[str, int]): company_id of the WarehousesInsertModel.

                - contact_email (str): contact_email of the WarehousesInsertModel.

                - contact_name (str): contact_name of the WarehousesInsertModel.

                - country_id (Union[str, int]): country_id of the WarehousesInsertModel.

                - fax (str): fax of the WarehousesInsertModel.

                - is_default (bool): is_default of the WarehousesInsertModel.

                - phone (str): phone of the WarehousesInsertModel.

                - title (str): title of the WarehousesInsertModel.

                - zip_code (str): zip_code of the WarehousesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/warehouses/update/", method="post")
    def update(self, data: Union[WarehousesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[WarehousesUpdateModel, dict], **kwargs)

        Args:

            data (Union[WarehousesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the WarehousesUpdateModel.

                - city (str): city of the WarehousesUpdateModel.

                - code (str): code of the WarehousesUpdateModel.

                - company_id (Union[str, int]): company_id of the WarehousesUpdateModel.

                - contact_email (str): contact_email of the WarehousesUpdateModel.

                - contact_name (str): contact_name of the WarehousesUpdateModel.

                - country_id (Union[str, int]): country_id of the WarehousesUpdateModel.

                - fax (str): fax of the WarehousesUpdateModel.

                - is_default (bool): is_default of the WarehousesUpdateModel.

                - phone (str): phone of the WarehousesUpdateModel.

                - title (str): title of the WarehousesUpdateModel.

                - warehouse_id (Union[str, int]): warehouse_id of the WarehousesUpdateModel.

                - zip_code (str): zip_code of the WarehousesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WarehousesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
