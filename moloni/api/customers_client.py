from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class CustomersCountModel(BaseModel):
    company_id: Union[str, int]


class CustomersCountByNameModel(BaseModel):
    company_id: Union[str, int]
    name: Optional[str] = None


class CustomersCountByNumberModel(BaseModel):
    company_id: Union[str, int]
    number: Optional[str] = None


class CustomersCountBySearchModel(BaseModel):
    company_id: Union[str, int]
    search: Optional[str] = None


class CustomersCountByVatModel(BaseModel):
    company_id: Union[str, int]
    vat: Optional[str] = None


class CustomersCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None


class CustomersDeleteModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None


class CustomersGetAllModel(BaseModel):
    company_id: Union[str, int]
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25


class CustomersGetByNameModel(BaseModel):
    company_id: Union[str, int]
    name: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25


class CustomersGetByNumberModel(BaseModel):
    company_id: Union[str, int]
    number: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25


class CustomersGetBySearchModel(BaseModel):
    company_id: Union[str, int]
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25
    search: Optional[str] = None


class CustomersGetByVatModel(BaseModel):
    company_id: Union[str, int]
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25
    vat: Optional[str] = None


class CustomersGetLastNumberModel(BaseModel):
    company_id: Union[str, int]


class CustomersGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25


class CustomersGetOneModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None


class CustomersInsertModel(BaseModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    city: Optional[str] = None
    contact_email: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    credit_limit: Optional[str] = None
    delivery_method_id: Optional[Union[str, int]] = None
    discount: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    field_notes: Optional[str] = None
    language_id: Optional[Union[str, int]] = None
    maturity_date_id: Optional[Union[str, int]] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    number: Optional[str] = None
    payment_day: Optional[str] = None
    payment_method_id: Optional[Union[str, int]] = None
    phone: Optional[str] = None
    qty_copies_document: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    vat: Optional[str] = None
    website: Optional[str] = None
    zip_code: Optional[str] = None


class CustomersUpdateModel(BaseModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    city: Optional[str] = None
    contact_email: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    credit_limit: Optional[str] = None
    customer_id: Optional[Union[str, int]] = None
    delivery_method_id: Optional[Union[str, int]] = None
    discount: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    field_notes: Optional[str] = None
    language_id: Optional[Union[str, int]] = None
    maturity_date_id: Optional[Union[str, int]] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    number: Optional[str] = None
    payment_day: Optional[str] = None
    payment_method_id: Optional[Union[str, int]] = None
    phone: Optional[str] = None
    qty_copies_document: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    vat: Optional[str] = None
    website: Optional[str] = None
    zip_code: Optional[str] = None


class CustomersClient(MoloniBaseClient):

    @endpoint("/<version>/customers/count/", method="post")
    def count(self, data: Union[CustomersCountModel, dict], **kwargs):
        """
        count(self, data: Union[CustomersCountModel, dict], **kwargs)

        Args:

            data (Union[CustomersCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/countByName/", method="post")
    def count_by_name(self, data: Union[CustomersCountByNameModel, dict], **kwargs):
        """
        count_by_name(self, data: Union[CustomersCountByNameModel, dict], **kwargs)

        Args:

            data (Union[CustomersCountByNameModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersCountByNameModel.

                - name (str): name of the CustomersCountByNameModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersCountByNameModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/countByNumber/", method="post")
    def count_by_number(self, data: Union[CustomersCountByNumberModel, dict], **kwargs):
        """
        count_by_number(self, data: Union[CustomersCountByNumberModel, dict], **kwargs)

        Args:

            data (Union[CustomersCountByNumberModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersCountByNumberModel.

                - number (str): number of the CustomersCountByNumberModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersCountByNumberModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/countBySearch/", method="post")
    def count_by_search(self, data: Union[CustomersCountBySearchModel, dict], **kwargs):
        """
        count_by_search(self, data: Union[CustomersCountBySearchModel, dict], **kwargs)

        Args:

            data (Union[CustomersCountBySearchModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersCountBySearchModel.

                - search (str): search of the CustomersCountBySearchModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersCountBySearchModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/countByVat/", method="post")
    def count_by_vat(self, data: Union[CustomersCountByVatModel, dict], **kwargs):
        """
        count_by_vat(self, data: Union[CustomersCountByVatModel, dict], **kwargs)

        Args:

            data (Union[CustomersCountByVatModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersCountByVatModel.

                - vat (str): vat of the CustomersCountByVatModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersCountByVatModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[CustomersCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[CustomersCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[CustomersCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the CustomersCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/delete/", method="post")
    def delete(self, data: Union[CustomersDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[CustomersDeleteModel, dict], **kwargs)

        Args:

            data (Union[CustomersDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersDeleteModel.

                - customer_id (Union[str, int]): customer_id of the CustomersDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/getAll/", method="post")
    def get_all(self, data: Union[CustomersGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[CustomersGetAllModel, dict], **kwargs)

        Args:

            data (Union[CustomersGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersGetAllModel.

                - offset (str): offset of the CustomersGetAllModel.

                - qty (str): qty of the CustomersGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/getByName/", method="post")
    def get_by_name(self, data: Union[CustomersGetByNameModel, dict], **kwargs):
        """
        get_by_name(self, data: Union[CustomersGetByNameModel, dict], **kwargs)

        Args:

            data (Union[CustomersGetByNameModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersGetByNameModel.

                - name (str): name of the CustomersGetByNameModel.

                - offset (str): offset of the CustomersGetByNameModel.

                - qty (str): qty of the CustomersGetByNameModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersGetByNameModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/getByNumber/", method="post")
    def get_by_number(self, data: Union[CustomersGetByNumberModel, dict], **kwargs):
        """
        get_by_number(self, data: Union[CustomersGetByNumberModel, dict], **kwargs)

        Args:

            data (Union[CustomersGetByNumberModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersGetByNumberModel.

                - number (str): number of the CustomersGetByNumberModel.

                - offset (str): offset of the CustomersGetByNumberModel.

                - qty (str): qty of the CustomersGetByNumberModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersGetByNumberModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/getBySearch/", method="post")
    def get_by_search(self, data: Union[CustomersGetBySearchModel, dict], **kwargs):
        """
        get_by_search(self, data: Union[CustomersGetBySearchModel, dict], **kwargs)

        Args:

            data (Union[CustomersGetBySearchModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersGetBySearchModel.

                - offset (str): offset of the CustomersGetBySearchModel.

                - qty (str): qty of the CustomersGetBySearchModel.

                - search (str): search of the CustomersGetBySearchModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersGetBySearchModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/getByVat/", method="post")
    def get_by_vat(self, data: Union[CustomersGetByVatModel, dict], **kwargs):
        """
        get_by_vat(self, data: Union[CustomersGetByVatModel, dict], **kwargs)

        Args:

            data (Union[CustomersGetByVatModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersGetByVatModel.

                - offset (str): offset of the CustomersGetByVatModel.

                - qty (str): qty of the CustomersGetByVatModel.

                - vat (str): vat of the CustomersGetByVatModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersGetByVatModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/getLastNumber/", method="post")
    def get_last_number(self, data: Union[CustomersGetLastNumberModel, dict], **kwargs):
        """
        get_last_number(self, data: Union[CustomersGetLastNumberModel, dict], **kwargs)

        Args:

            data (Union[CustomersGetLastNumberModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersGetLastNumberModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersGetLastNumberModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[CustomersGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[CustomersGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[CustomersGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the CustomersGetModifiedSinceModel.

                - offset (str): offset of the CustomersGetModifiedSinceModel.

                - qty (str): qty of the CustomersGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/getOne/", method="post")
    def get_one(self, data: Union[CustomersGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[CustomersGetOneModel, dict], **kwargs)

        Args:

            data (Union[CustomersGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomersGetOneModel.

                - customer_id (Union[str, int]): customer_id of the CustomersGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/insert/", method="post")
    def insert(self, data: Union[CustomersInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[CustomersInsertModel, dict], **kwargs)

        Args:

            data (Union[CustomersInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the CustomersInsertModel.

                - city (str): city of the CustomersInsertModel.

                - company_id (Union[str, int]): company_id of the CustomersInsertModel.

                - contact_email (str): contact_email of the CustomersInsertModel.

                - contact_name (str): contact_name of the CustomersInsertModel.

                - contact_phone (str): contact_phone of the CustomersInsertModel.

                - country_id (Union[str, int]): country_id of the CustomersInsertModel.

                - credit_limit (str): credit_limit of the CustomersInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the CustomersInsertModel.

                - discount (str): discount of the CustomersInsertModel.

                - email (str): email of the CustomersInsertModel.

                - fax (str): fax of the CustomersInsertModel.

                - field_notes (str): field_notes of the CustomersInsertModel.

                - language_id (Union[str, int]): language_id of the CustomersInsertModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the CustomersInsertModel.

                - name (str): name of the CustomersInsertModel.

                - notes (str): notes of the CustomersInsertModel.

                - number (str): number of the CustomersInsertModel.

                - payment_day (str): payment_day of the CustomersInsertModel.

                - payment_method_id (Union[str, int]): payment_method_id of the CustomersInsertModel.

                - phone (str): phone of the CustomersInsertModel.

                - qty_copies_document (str): qty_copies_document of the CustomersInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the CustomersInsertModel.

                - vat (str): vat of the CustomersInsertModel.

                - website (str): website of the CustomersInsertModel.

                - zip_code (str): zip_code of the CustomersInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customers/update/", method="post")
    def update(self, data: Union[CustomersUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[CustomersUpdateModel, dict], **kwargs)

        Args:

            data (Union[CustomersUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the CustomersUpdateModel.

                - city (str): city of the CustomersUpdateModel.

                - company_id (Union[str, int]): company_id of the CustomersUpdateModel.

                - contact_email (str): contact_email of the CustomersUpdateModel.

                - contact_name (str): contact_name of the CustomersUpdateModel.

                - contact_phone (str): contact_phone of the CustomersUpdateModel.

                - country_id (Union[str, int]): country_id of the CustomersUpdateModel.

                - credit_limit (str): credit_limit of the CustomersUpdateModel.

                - customer_id (Union[str, int]): customer_id of the CustomersUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the CustomersUpdateModel.

                - discount (str): discount of the CustomersUpdateModel.

                - email (str): email of the CustomersUpdateModel.

                - fax (str): fax of the CustomersUpdateModel.

                - field_notes (str): field_notes of the CustomersUpdateModel.

                - language_id (Union[str, int]): language_id of the CustomersUpdateModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the CustomersUpdateModel.

                - name (str): name of the CustomersUpdateModel.

                - notes (str): notes of the CustomersUpdateModel.

                - number (str): number of the CustomersUpdateModel.

                - payment_day (str): payment_day of the CustomersUpdateModel.

                - payment_method_id (Union[str, int]): payment_method_id of the CustomersUpdateModel.

                - phone (str): phone of the CustomersUpdateModel.

                - qty_copies_document (str): qty_copies_document of the CustomersUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the CustomersUpdateModel.

                - vat (str): vat of the CustomersUpdateModel.

                - website (str): website of the CustomersUpdateModel.

                - zip_code (str): zip_code of the CustomersUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomersUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
