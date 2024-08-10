from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ReceiptsCountModel(BaseModel):
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


class ReceiptsDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]


class ReceiptsGetAllModel(BaseModel):
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


class ReceiptsGetOneModel(BaseModel):
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


class ReceiptsInsertModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    net_value: str
    notes: str
    related_documents_notes: str
    status: str
    associated_documents: str = None
    payments: str = None


class ReceiptsUpdateModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]
    associated_documents: str = None
    customer_id: Union[str, int] = None
    date: str = None
    document_set_id: Union[str, int] = None
    net_value: str = None
    notes: str = None
    payments: str = None
    related_documents_notes: str = None
    status: str = None


class ReceiptsClient(MoloniBaseClient):

    @endpoint("/<version>/receipts/count/", method="post")
    def count(self, data: Union[ReceiptsCountModel, dict], **kwargs):
        """
        count(self, data: Union[ReceiptsCountModel, dict], **kwargs)

        Args:

            data (Union[ReceiptsCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ReceiptsCountModel.

                - customer_id (Union[str, int]): customer_id of the ReceiptsCountModel.

                - date (str): date of the ReceiptsCountModel.

                - document_set_id (Union[str, int]): document_set_id of the ReceiptsCountModel.

                - expiration_date (str): expiration_date of the ReceiptsCountModel.

                - number (str): number of the ReceiptsCountModel.

                - our_reference (str): our_reference of the ReceiptsCountModel.

                - salesman_id (Union[str, int]): salesman_id of the ReceiptsCountModel.

                - supplier_id (Union[str, int]): supplier_id of the ReceiptsCountModel.

                - year (str): year of the ReceiptsCountModel.

                - your_reference (str): your_reference of the ReceiptsCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ReceiptsCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/receipts/delete/", method="post")
    def delete(self, data: Union[ReceiptsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[ReceiptsDeleteModel, dict], **kwargs)

        Args:

            data (Union[ReceiptsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ReceiptsDeleteModel.

                - document_id (Union[str, int]): document_id of the ReceiptsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ReceiptsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/receipts/getAll/", method="post")
    def get_all(self, data: Union[ReceiptsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[ReceiptsGetAllModel, dict], **kwargs)

        Args:

            data (Union[ReceiptsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ReceiptsGetAllModel.

                - customer_id (Union[str, int]): customer_id of the ReceiptsGetAllModel.

                - date (str): date of the ReceiptsGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the ReceiptsGetAllModel.

                - expiration_date (str): expiration_date of the ReceiptsGetAllModel.

                - number (str): number of the ReceiptsGetAllModel.

                - offset (str): offset of the ReceiptsGetAllModel.

                - our_reference (str): our_reference of the ReceiptsGetAllModel.

                - qty (str): qty of the ReceiptsGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the ReceiptsGetAllModel.

                - supplier_id (Union[str, int]): supplier_id of the ReceiptsGetAllModel.

                - year (str): year of the ReceiptsGetAllModel.

                - your_reference (str): your_reference of the ReceiptsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ReceiptsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/receipts/getOne/", method="post")
    def get_one(self, data: Union[ReceiptsGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[ReceiptsGetOneModel, dict], **kwargs)

        Args:

            data (Union[ReceiptsGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ReceiptsGetOneModel.

                - customer_id (Union[str, int]): customer_id of the ReceiptsGetOneModel.

                - date (str): date of the ReceiptsGetOneModel.

                - document_id (Union[str, int]): document_id of the ReceiptsGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the ReceiptsGetOneModel.

                - expiration_date (str): expiration_date of the ReceiptsGetOneModel.

                - number (str): number of the ReceiptsGetOneModel.

                - our_reference (str): our_reference of the ReceiptsGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the ReceiptsGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the ReceiptsGetOneModel.

                - year (str): year of the ReceiptsGetOneModel.

                - your_reference (str): your_reference of the ReceiptsGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ReceiptsGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/receipts/insert/", method="post")
    def insert(self, data: Union[ReceiptsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[ReceiptsInsertModel, dict], **kwargs)

        Args:

            data (Union[ReceiptsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the ReceiptsInsertModel.

                - company_id (Union[str, int]): company_id of the ReceiptsInsertModel.

                - customer_id (Union[str, int]): customer_id of the ReceiptsInsertModel.

                - date (str): date of the ReceiptsInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the ReceiptsInsertModel.

                - net_value (str): net_value of the ReceiptsInsertModel.

                - notes (str): notes of the ReceiptsInsertModel.

                - payments (str): payments of the ReceiptsInsertModel.

                - related_documents_notes (str): related_documents_notes of the ReceiptsInsertModel.

                - status (str): status of the ReceiptsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ReceiptsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/receipts/update/", method="post")
    def update(self, data: Union[ReceiptsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[ReceiptsUpdateModel, dict], **kwargs)

        Args:

            data (Union[ReceiptsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the ReceiptsUpdateModel.

                - company_id (Union[str, int]): company_id of the ReceiptsUpdateModel.

                - customer_id (Union[str, int]): customer_id of the ReceiptsUpdateModel.

                - date (str): date of the ReceiptsUpdateModel.

                - document_id (Union[str, int]): document_id of the ReceiptsUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the ReceiptsUpdateModel.

                - net_value (str): net_value of the ReceiptsUpdateModel.

                - notes (str): notes of the ReceiptsUpdateModel.

                - payments (str): payments of the ReceiptsUpdateModel.

                - related_documents_notes (str): related_documents_notes of the ReceiptsUpdateModel.

                - status (str): status of the ReceiptsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ReceiptsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
