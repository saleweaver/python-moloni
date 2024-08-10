from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class SuppliersCountModel(BaseModel):
    company_id: Union[str, int]


class SuppliersCountByNameModel(BaseModel):
    company_id: Union[str, int]
    name: str


class SuppliersCountByNumberModel(BaseModel):
    company_id: Union[str, int]
    number: str


class SuppliersCountBySearchModel(BaseModel):
    company_id: Union[str, int]
    search: str


class SuppliersCountByVatModel(BaseModel):
    company_id: Union[str, int]
    vat: str


class SuppliersCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class SuppliersDeleteModel(BaseModel):
    company_id: Union[str, int]
    supplier_id: Union[str, int]


class SuppliersGetAllModel(BaseModel):
    company_id: Union[str, int]
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25


class SuppliersGetByNameModel(BaseModel):
    company_id: Union[str, int]
    name: str
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25


class SuppliersGetByNumberModel(BaseModel):
    company_id: Union[str, int]
    number: str
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25


class SuppliersGetBySearchModel(BaseModel):
    company_id: Union[str, int]
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25
    search: str


class SuppliersGetByVatModel(BaseModel):
    company_id: Union[str, int]
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25
    vat: str


class SuppliersGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25


class SuppliersGetOneModel(BaseModel):
    company_id: Union[str, int]
    supplier_id: Union[str, int]


class SuppliersInsertModel(BaseModel):
    address: str
    city: str
    company_id: Union[str, int]
    contact_email: str
    contact_name: str
    contact_phone: str
    country_id: Union[str, int]
    credit_limit: str
    delivery_method_id: Union[str, int]
    discount: str
    email: str
    fax: str
    field_notes: str
    language_id: Union[str, int]
    maturity_date_id: Union[str, int]
    name: str
    notes: str
    number: str
    payment_method_id: Union[str, int]
    phone: str
    qty_copies_document: str
    vat: str
    website: str
    zip_code: str


class SuppliersUpdateModel(BaseModel):
    company_id: Union[str, int]
    supplier_id: Union[str, int]
    address: str = None
    city: str = None
    contact_email: str = None
    contact_name: str = None
    contact_phone: str = None
    country_id: Union[str, int] = None
    credit_limit: str = None
    delivery_method_id: Union[str, int] = None
    discount: str = None
    email: str = None
    fax: str = None
    field_notes: str = None
    language_id: Union[str, int] = None
    maturity_date_id: Union[str, int] = None
    name: str = None
    notes: str = None
    number: str = None
    payment_method_id: Union[str, int] = None
    phone: str = None
    qty_copies_document: str = None
    vat: str = None
    website: str = None
    zip_code: str = None


class SuppliersClient(MoloniBaseClient):

    @endpoint("/<version>/suppliers/count/", method="post")
    def count(self, data: Union[SuppliersCountModel, dict], **kwargs):
        """
        count(self, data: Union[SuppliersCountModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countByName/", method="post")
    def count_by_name(self, data: Union[SuppliersCountByNameModel, dict], **kwargs):
        """
        count_by_name(self, data: Union[SuppliersCountByNameModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountByNameModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountByNameModel.

                - name (str): name of the SuppliersCountByNameModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountByNameModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countByNumber/", method="post")
    def count_by_number(self, data: Union[SuppliersCountByNumberModel, dict], **kwargs):
        """
        count_by_number(self, data: Union[SuppliersCountByNumberModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountByNumberModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountByNumberModel.

                - number (str): number of the SuppliersCountByNumberModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountByNumberModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countBySearch/", method="post")
    def count_by_search(self, data: Union[SuppliersCountBySearchModel, dict], **kwargs):
        """
        count_by_search(self, data: Union[SuppliersCountBySearchModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountBySearchModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountBySearchModel.

                - search (str): search of the SuppliersCountBySearchModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountBySearchModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countByVat/", method="post")
    def count_by_vat(self, data: Union[SuppliersCountByVatModel, dict], **kwargs):
        """
        count_by_vat(self, data: Union[SuppliersCountByVatModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountByVatModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountByVatModel.

                - vat (str): vat of the SuppliersCountByVatModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountByVatModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[SuppliersCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[SuppliersCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the SuppliersCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/delete/", method="post")
    def delete(self, data: Union[SuppliersDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[SuppliersDeleteModel, dict], **kwargs)

        Args:

            data (Union[SuppliersDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersDeleteModel.

                - supplier_id (Union[str, int]): supplier_id of the SuppliersDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getAll/", method="post")
    def get_all(self, data: Union[SuppliersGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[SuppliersGetAllModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetAllModel.

                - offset (str): offset of the SuppliersGetAllModel.

                - qty (str): qty of the SuppliersGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getByName/", method="post")
    def get_by_name(self, data: Union[SuppliersGetByNameModel, dict], **kwargs):
        """
        get_by_name(self, data: Union[SuppliersGetByNameModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetByNameModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetByNameModel.

                - name (str): name of the SuppliersGetByNameModel.

                - offset (str): offset of the SuppliersGetByNameModel.

                - qty (str): qty of the SuppliersGetByNameModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetByNameModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getByNumber/", method="post")
    def get_by_number(self, data: Union[SuppliersGetByNumberModel, dict], **kwargs):
        """
        get_by_number(self, data: Union[SuppliersGetByNumberModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetByNumberModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetByNumberModel.

                - number (str): number of the SuppliersGetByNumberModel.

                - offset (str): offset of the SuppliersGetByNumberModel.

                - qty (str): qty of the SuppliersGetByNumberModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetByNumberModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getBySearch/", method="post")
    def get_by_search(self, data: Union[SuppliersGetBySearchModel, dict], **kwargs):
        """
        get_by_search(self, data: Union[SuppliersGetBySearchModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetBySearchModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetBySearchModel.

                - offset (str): offset of the SuppliersGetBySearchModel.

                - qty (str): qty of the SuppliersGetBySearchModel.

                - search (str): search of the SuppliersGetBySearchModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetBySearchModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getByVat/", method="post")
    def get_by_vat(self, data: Union[SuppliersGetByVatModel, dict], **kwargs):
        """
        get_by_vat(self, data: Union[SuppliersGetByVatModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetByVatModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetByVatModel.

                - offset (str): offset of the SuppliersGetByVatModel.

                - qty (str): qty of the SuppliersGetByVatModel.

                - vat (str): vat of the SuppliersGetByVatModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetByVatModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[SuppliersGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[SuppliersGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the SuppliersGetModifiedSinceModel.

                - offset (str): offset of the SuppliersGetModifiedSinceModel.

                - qty (str): qty of the SuppliersGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getOne/", method="post")
    def get_one(self, data: Union[SuppliersGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[SuppliersGetOneModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the SuppliersGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/insert/", method="post")
    def insert(self, data: Union[SuppliersInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[SuppliersInsertModel, dict], **kwargs)

        Args:

            data (Union[SuppliersInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the SuppliersInsertModel.

                - city (str): city of the SuppliersInsertModel.

                - company_id (Union[str, int]): company_id of the SuppliersInsertModel.

                - contact_email (str): contact_email of the SuppliersInsertModel.

                - contact_name (str): contact_name of the SuppliersInsertModel.

                - contact_phone (str): contact_phone of the SuppliersInsertModel.

                - country_id (Union[str, int]): country_id of the SuppliersInsertModel.

                - credit_limit (str): credit_limit of the SuppliersInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the SuppliersInsertModel.

                - discount (str): discount of the SuppliersInsertModel.

                - email (str): email of the SuppliersInsertModel.

                - fax (str): fax of the SuppliersInsertModel.

                - field_notes (str): field_notes of the SuppliersInsertModel.

                - language_id (Union[str, int]): language_id of the SuppliersInsertModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the SuppliersInsertModel.

                - name (str): name of the SuppliersInsertModel.

                - notes (str): notes of the SuppliersInsertModel.

                - number (str): number of the SuppliersInsertModel.

                - payment_method_id (Union[str, int]): payment_method_id of the SuppliersInsertModel.

                - phone (str): phone of the SuppliersInsertModel.

                - qty_copies_document (str): qty_copies_document of the SuppliersInsertModel.

                - vat (str): vat of the SuppliersInsertModel.

                - website (str): website of the SuppliersInsertModel.

                - zip_code (str): zip_code of the SuppliersInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/update/", method="post")
    def update(self, data: Union[SuppliersUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[SuppliersUpdateModel, dict], **kwargs)

        Args:

            data (Union[SuppliersUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the SuppliersUpdateModel.

                - city (str): city of the SuppliersUpdateModel.

                - company_id (Union[str, int]): company_id of the SuppliersUpdateModel.

                - contact_email (str): contact_email of the SuppliersUpdateModel.

                - contact_name (str): contact_name of the SuppliersUpdateModel.

                - contact_phone (str): contact_phone of the SuppliersUpdateModel.

                - country_id (Union[str, int]): country_id of the SuppliersUpdateModel.

                - credit_limit (str): credit_limit of the SuppliersUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the SuppliersUpdateModel.

                - discount (str): discount of the SuppliersUpdateModel.

                - email (str): email of the SuppliersUpdateModel.

                - fax (str): fax of the SuppliersUpdateModel.

                - field_notes (str): field_notes of the SuppliersUpdateModel.

                - language_id (Union[str, int]): language_id of the SuppliersUpdateModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the SuppliersUpdateModel.

                - name (str): name of the SuppliersUpdateModel.

                - notes (str): notes of the SuppliersUpdateModel.

                - number (str): number of the SuppliersUpdateModel.

                - payment_method_id (Union[str, int]): payment_method_id of the SuppliersUpdateModel.

                - phone (str): phone of the SuppliersUpdateModel.

                - qty_copies_document (str): qty_copies_document of the SuppliersUpdateModel.

                - supplier_id (Union[str, int]): supplier_id of the SuppliersUpdateModel.

                - vat (str): vat of the SuppliersUpdateModel.

                - website (str): website of the SuppliersUpdateModel.

                - zip_code (str): zip_code of the SuppliersUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
