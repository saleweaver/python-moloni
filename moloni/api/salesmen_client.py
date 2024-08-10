from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class SalesmenCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class SalesmenDeleteModel(BaseModel):
    company_id: Union[str, int]
    salesman_id: Union[str, int]


class SalesmenGetAllModel(BaseModel):
    company_id: Union[str, int]


class SalesmenGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class SalesmenGetOneModel(BaseModel):
    company_id: Union[str, int]
    salesman_id: Union[str, int]


class SalesmenInsertModel(BaseModel):
    address: str
    base_commission: str
    city: str
    company_id: Union[str, int]
    country_id: Union[str, int]
    email: str
    fax: str
    language_id: Union[str, int]
    name: str
    notes: str
    number: str
    phone: str
    qty_copies_document: str
    vat: str
    website: str
    zip_code: str


class SalesmenUpdateModel(BaseModel):
    company_id: Union[str, int]
    salesman_id: Union[str, int]
    address: str = None
    base_commission: str = None
    city: str = None
    country_id: Union[str, int] = None
    email: str = None
    fax: str = None
    language_id: Union[str, int] = None
    name: str = None
    notes: str = None
    number: str = None
    phone: str = None
    qty_copies_document: str = None
    vat: str = None
    website: str = None
    zip_code: str = None


class SalesmenClient(MoloniBaseClient):

    @endpoint("/<version>/salesmen/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[SalesmenCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[SalesmenCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[SalesmenCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the SalesmenCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/delete/", method="post")
    def delete(self, data: Union[SalesmenDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[SalesmenDeleteModel, dict], **kwargs)

        Args:

            data (Union[SalesmenDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenDeleteModel.

                - salesman_id (Union[str, int]): salesman_id of the SalesmenDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/getAll/", method="post")
    def get_all(self, data: Union[SalesmenGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[SalesmenGetAllModel, dict], **kwargs)

        Args:

            data (Union[SalesmenGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[SalesmenGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[SalesmenGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[SalesmenGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the SalesmenGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/getOne/", method="post")
    def get_one(self, data: Union[SalesmenGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[SalesmenGetOneModel, dict], **kwargs)

        Args:

            data (Union[SalesmenGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SalesmenGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the SalesmenGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/insert/", method="post")
    def insert(self, data: Union[SalesmenInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[SalesmenInsertModel, dict], **kwargs)

        Args:

            data (Union[SalesmenInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the SalesmenInsertModel.

                - base_commission (str): base_commission of the SalesmenInsertModel.

                - city (str): city of the SalesmenInsertModel.

                - company_id (Union[str, int]): company_id of the SalesmenInsertModel.

                - country_id (Union[str, int]): country_id of the SalesmenInsertModel.

                - email (str): email of the SalesmenInsertModel.

                - fax (str): fax of the SalesmenInsertModel.

                - language_id (Union[str, int]): language_id of the SalesmenInsertModel.

                - name (str): name of the SalesmenInsertModel.

                - notes (str): notes of the SalesmenInsertModel.

                - number (str): number of the SalesmenInsertModel.

                - phone (str): phone of the SalesmenInsertModel.

                - qty_copies_document (str): qty_copies_document of the SalesmenInsertModel.

                - vat (str): vat of the SalesmenInsertModel.

                - website (str): website of the SalesmenInsertModel.

                - zip_code (str): zip_code of the SalesmenInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/salesmen/update/", method="post")
    def update(self, data: Union[SalesmenUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[SalesmenUpdateModel, dict], **kwargs)

        Args:

            data (Union[SalesmenUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the SalesmenUpdateModel.

                - base_commission (str): base_commission of the SalesmenUpdateModel.

                - city (str): city of the SalesmenUpdateModel.

                - company_id (Union[str, int]): company_id of the SalesmenUpdateModel.

                - country_id (Union[str, int]): country_id of the SalesmenUpdateModel.

                - email (str): email of the SalesmenUpdateModel.

                - fax (str): fax of the SalesmenUpdateModel.

                - language_id (Union[str, int]): language_id of the SalesmenUpdateModel.

                - name (str): name of the SalesmenUpdateModel.

                - notes (str): notes of the SalesmenUpdateModel.

                - number (str): number of the SalesmenUpdateModel.

                - phone (str): phone of the SalesmenUpdateModel.

                - qty_copies_document (str): qty_copies_document of the SalesmenUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the SalesmenUpdateModel.

                - vat (str): vat of the SalesmenUpdateModel.

                - website (str): website of the SalesmenUpdateModel.

                - zip_code (str): zip_code of the SalesmenUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SalesmenUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
