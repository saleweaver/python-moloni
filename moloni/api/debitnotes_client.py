from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class DebitnotesCountModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    our_reference: str
    salesman_id: Union[str, int]
    supplier_id: Union[str, int]
    year: str
    your_reference: str


class DebitnotesDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]


class DebitnotesGetAllModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    offset: Union[str, int] = 0
    our_reference: str
    qty: Union[str, int] = 25
    salesman_id: Union[str, int]
    supplier_id: Union[str, int]
    year: str
    your_reference: str


class DebitnotesGetOneModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_id: Union[str, int]
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    our_reference: str
    salesman_id: Union[str, int]
    supplier_id: Union[str, int]
    year: str
    your_reference: str


class DebitnotesInsertModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    expiration_date: str
    notes: str
    salesman_commission: str
    salesman_id: Union[str, int]
    status: str
    your_reference: str
    products: str = None


class DebitnotesUpdateModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]
    customer_id: Union[str, int] = None
    date: str = None
    document_set_id: Union[str, int] = None
    expiration_date: str = None
    notes: str = None
    products: str = None
    salesman_commission: str = None
    salesman_id: Union[str, int] = None
    status: str = None
    your_reference: str = None


class DebitnotesClient(MoloniBaseClient):

    @endpoint("/<version>/debitNotes/count/", method="post")
    def count(self, data: Union[DebitnotesCountModel, dict], **kwargs):
        """
        count(self, data: Union[DebitnotesCountModel, dict], **kwargs)

        Args:

            data (Union[DebitnotesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DebitnotesCountModel.

                - customer_id (Union[str, int]): customer_id of the DebitnotesCountModel.

                - date (str): date of the DebitnotesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the DebitnotesCountModel.

                - expiration_date (str): expiration_date of the DebitnotesCountModel.

                - number (str): number of the DebitnotesCountModel.

                - our_reference (str): our_reference of the DebitnotesCountModel.

                - salesman_id (Union[str, int]): salesman_id of the DebitnotesCountModel.

                - supplier_id (Union[str, int]): supplier_id of the DebitnotesCountModel.

                - year (str): year of the DebitnotesCountModel.

                - your_reference (str): your_reference of the DebitnotesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DebitnotesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/debitNotes/delete/", method="post")
    def delete(self, data: Union[DebitnotesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[DebitnotesDeleteModel, dict], **kwargs)

        Args:

            data (Union[DebitnotesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DebitnotesDeleteModel.

                - document_id (Union[str, int]): document_id of the DebitnotesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DebitnotesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/debitNotes/getAll/", method="post")
    def get_all(self, data: Union[DebitnotesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[DebitnotesGetAllModel, dict], **kwargs)

        Args:

            data (Union[DebitnotesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DebitnotesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the DebitnotesGetAllModel.

                - date (str): date of the DebitnotesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the DebitnotesGetAllModel.

                - expiration_date (str): expiration_date of the DebitnotesGetAllModel.

                - number (str): number of the DebitnotesGetAllModel.

                - offset (str): offset of the DebitnotesGetAllModel.

                - our_reference (str): our_reference of the DebitnotesGetAllModel.

                - qty (str): qty of the DebitnotesGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the DebitnotesGetAllModel.

                - supplier_id (Union[str, int]): supplier_id of the DebitnotesGetAllModel.

                - year (str): year of the DebitnotesGetAllModel.

                - your_reference (str): your_reference of the DebitnotesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DebitnotesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/debitNotes/getOne/", method="post")
    def get_one(self, data: Union[DebitnotesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[DebitnotesGetOneModel, dict], **kwargs)

        Args:

            data (Union[DebitnotesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DebitnotesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the DebitnotesGetOneModel.

                - date (str): date of the DebitnotesGetOneModel.

                - document_id (Union[str, int]): document_id of the DebitnotesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the DebitnotesGetOneModel.

                - expiration_date (str): expiration_date of the DebitnotesGetOneModel.

                - number (str): number of the DebitnotesGetOneModel.

                - our_reference (str): our_reference of the DebitnotesGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the DebitnotesGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the DebitnotesGetOneModel.

                - year (str): year of the DebitnotesGetOneModel.

                - your_reference (str): your_reference of the DebitnotesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DebitnotesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/debitNotes/insert/", method="post")
    def insert(self, data: Union[DebitnotesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[DebitnotesInsertModel, dict], **kwargs)

        Args:

            data (Union[DebitnotesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DebitnotesInsertModel.

                - customer_id (Union[str, int]): customer_id of the DebitnotesInsertModel.

                - date (str): date of the DebitnotesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the DebitnotesInsertModel.

                - expiration_date (str): expiration_date of the DebitnotesInsertModel.

                - notes (str): notes of the DebitnotesInsertModel.

                - products (str): products of the DebitnotesInsertModel.

                - salesman_commission (str): salesman_commission of the DebitnotesInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the DebitnotesInsertModel.

                - status (str): status of the DebitnotesInsertModel.

                - your_reference (str): your_reference of the DebitnotesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DebitnotesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/debitNotes/update/", method="post")
    def update(self, data: Union[DebitnotesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[DebitnotesUpdateModel, dict], **kwargs)

        Args:

            data (Union[DebitnotesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DebitnotesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the DebitnotesUpdateModel.

                - date (str): date of the DebitnotesUpdateModel.

                - document_id (Union[str, int]): document_id of the DebitnotesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the DebitnotesUpdateModel.

                - expiration_date (str): expiration_date of the DebitnotesUpdateModel.

                - notes (str): notes of the DebitnotesUpdateModel.

                - products (str): products of the DebitnotesUpdateModel.

                - salesman_commission (str): salesman_commission of the DebitnotesUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the DebitnotesUpdateModel.

                - status (str): status of the DebitnotesUpdateModel.

                - your_reference (str): your_reference of the DebitnotesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DebitnotesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
