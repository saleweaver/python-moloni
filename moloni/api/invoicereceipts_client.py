from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class InvoicereceiptsCountModel(BaseModel):
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


class InvoicereceiptsDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]


class InvoicereceiptsGetAllModel(BaseModel):
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


class InvoicereceiptsGetOneModel(BaseModel):
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


class InvoicereceiptsInsertModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    deduction_id: Union[str, int]
    delivery_datetime: str
    delivery_departure_address: str
    delivery_departure_city: str
    delivery_departure_country: str
    delivery_departure_zip_code: str
    delivery_destination_address: str
    delivery_destination_city: str
    delivery_destination_country: str
    delivery_destination_zip_code: str
    delivery_method_id: Union[str, int]
    document_set_id: Union[str, int]
    expiration_date: str
    financial_discount: str
    notes: str
    our_reference: str
    related_documents_notes: str
    salesman_commission: str
    salesman_id: Union[str, int]
    special_discount: str
    status: str
    vehicle_id: Union[str, int]
    your_reference: str
    associated_documents: str = None
    payments: str = None
    products: str = None


class InvoicereceiptsUpdateModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]
    associated_documents: str = None
    customer_id: Union[str, int] = None
    date: str = None
    deduction_id: Union[str, int] = None
    delivery_datetime: str = None
    delivery_departure_address: str = None
    delivery_departure_city: str = None
    delivery_departure_country: str = None
    delivery_departure_zip_code: str = None
    delivery_destination_address: str = None
    delivery_destination_city: str = None
    delivery_destination_country: str = None
    delivery_destination_zip_code: str = None
    delivery_method_id: Union[str, int] = None
    document_set_id: Union[str, int] = None
    expiration_date: str = None
    financial_discount: str = None
    notes: str = None
    our_reference: str = None
    payments: str = None
    products: str = None
    related_documents_notes: str = None
    salesman_commission: str = None
    salesman_id: Union[str, int] = None
    special_discount: str = None
    status: str = None
    vehicle_id: Union[str, int] = None
    your_reference: str = None


class InvoicereceiptsClient(MoloniBaseClient):

    @endpoint("/<version>/invoiceReceipts/count/", method="post")
    def count(self, data: Union[InvoicereceiptsCountModel, dict], **kwargs):
        """
        count(self, data: Union[InvoicereceiptsCountModel, dict], **kwargs)

        Args:

            data (Union[InvoicereceiptsCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the InvoicereceiptsCountModel.

                - customer_id (Union[str, int]): customer_id of the InvoicereceiptsCountModel.

                - date (str): date of the InvoicereceiptsCountModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicereceiptsCountModel.

                - expiration_date (str): expiration_date of the InvoicereceiptsCountModel.

                - number (str): number of the InvoicereceiptsCountModel.

                - our_reference (str): our_reference of the InvoicereceiptsCountModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicereceiptsCountModel.

                - supplier_id (Union[str, int]): supplier_id of the InvoicereceiptsCountModel.

                - year (str): year of the InvoicereceiptsCountModel.

                - your_reference (str): your_reference of the InvoicereceiptsCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicereceiptsCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoiceReceipts/delete/", method="post")
    def delete(self, data: Union[InvoicereceiptsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[InvoicereceiptsDeleteModel, dict], **kwargs)

        Args:

            data (Union[InvoicereceiptsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the InvoicereceiptsDeleteModel.

                - document_id (Union[str, int]): document_id of the InvoicereceiptsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicereceiptsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoiceReceipts/getAll/", method="post")
    def get_all(self, data: Union[InvoicereceiptsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[InvoicereceiptsGetAllModel, dict], **kwargs)

        Args:

            data (Union[InvoicereceiptsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the InvoicereceiptsGetAllModel.

                - customer_id (Union[str, int]): customer_id of the InvoicereceiptsGetAllModel.

                - date (str): date of the InvoicereceiptsGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicereceiptsGetAllModel.

                - expiration_date (str): expiration_date of the InvoicereceiptsGetAllModel.

                - number (str): number of the InvoicereceiptsGetAllModel.

                - offset (str): offset of the InvoicereceiptsGetAllModel.

                - our_reference (str): our_reference of the InvoicereceiptsGetAllModel.

                - qty (str): qty of the InvoicereceiptsGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicereceiptsGetAllModel.

                - supplier_id (Union[str, int]): supplier_id of the InvoicereceiptsGetAllModel.

                - year (str): year of the InvoicereceiptsGetAllModel.

                - your_reference (str): your_reference of the InvoicereceiptsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicereceiptsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoiceReceipts/getOne/", method="post")
    def get_one(self, data: Union[InvoicereceiptsGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[InvoicereceiptsGetOneModel, dict], **kwargs)

        Args:

            data (Union[InvoicereceiptsGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the InvoicereceiptsGetOneModel.

                - customer_id (Union[str, int]): customer_id of the InvoicereceiptsGetOneModel.

                - date (str): date of the InvoicereceiptsGetOneModel.

                - document_id (Union[str, int]): document_id of the InvoicereceiptsGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicereceiptsGetOneModel.

                - expiration_date (str): expiration_date of the InvoicereceiptsGetOneModel.

                - number (str): number of the InvoicereceiptsGetOneModel.

                - our_reference (str): our_reference of the InvoicereceiptsGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicereceiptsGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the InvoicereceiptsGetOneModel.

                - year (str): year of the InvoicereceiptsGetOneModel.

                - your_reference (str): your_reference of the InvoicereceiptsGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicereceiptsGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoiceReceipts/insert/", method="post")
    def insert(self, data: Union[InvoicereceiptsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[InvoicereceiptsInsertModel, dict], **kwargs)

        Args:

            data (Union[InvoicereceiptsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the InvoicereceiptsInsertModel.

                - company_id (Union[str, int]): company_id of the InvoicereceiptsInsertModel.

                - customer_id (Union[str, int]): customer_id of the InvoicereceiptsInsertModel.

                - date (str): date of the InvoicereceiptsInsertModel.

                - deduction_id (Union[str, int]): deduction_id of the InvoicereceiptsInsertModel.

                - delivery_datetime (str): delivery_datetime of the InvoicereceiptsInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the InvoicereceiptsInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the InvoicereceiptsInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the InvoicereceiptsInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the InvoicereceiptsInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the InvoicereceiptsInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the InvoicereceiptsInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the InvoicereceiptsInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the InvoicereceiptsInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the InvoicereceiptsInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicereceiptsInsertModel.

                - expiration_date (str): expiration_date of the InvoicereceiptsInsertModel.

                - financial_discount (str): financial_discount of the InvoicereceiptsInsertModel.

                - notes (str): notes of the InvoicereceiptsInsertModel.

                - our_reference (str): our_reference of the InvoicereceiptsInsertModel.

                - payments (str): payments of the InvoicereceiptsInsertModel.

                - products (str): products of the InvoicereceiptsInsertModel.

                - related_documents_notes (str): related_documents_notes of the InvoicereceiptsInsertModel.

                - salesman_commission (str): salesman_commission of the InvoicereceiptsInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicereceiptsInsertModel.

                - special_discount (str): special_discount of the InvoicereceiptsInsertModel.

                - status (str): status of the InvoicereceiptsInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the InvoicereceiptsInsertModel.

                - your_reference (str): your_reference of the InvoicereceiptsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicereceiptsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoiceReceipts/update/", method="post")
    def update(self, data: Union[InvoicereceiptsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[InvoicereceiptsUpdateModel, dict], **kwargs)

        Args:

            data (Union[InvoicereceiptsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the InvoicereceiptsUpdateModel.

                - company_id (Union[str, int]): company_id of the InvoicereceiptsUpdateModel.

                - customer_id (Union[str, int]): customer_id of the InvoicereceiptsUpdateModel.

                - date (str): date of the InvoicereceiptsUpdateModel.

                - deduction_id (Union[str, int]): deduction_id of the InvoicereceiptsUpdateModel.

                - delivery_datetime (str): delivery_datetime of the InvoicereceiptsUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the InvoicereceiptsUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the InvoicereceiptsUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the InvoicereceiptsUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the InvoicereceiptsUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the InvoicereceiptsUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the InvoicereceiptsUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the InvoicereceiptsUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the InvoicereceiptsUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the InvoicereceiptsUpdateModel.

                - document_id (Union[str, int]): document_id of the InvoicereceiptsUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicereceiptsUpdateModel.

                - expiration_date (str): expiration_date of the InvoicereceiptsUpdateModel.

                - financial_discount (str): financial_discount of the InvoicereceiptsUpdateModel.

                - notes (str): notes of the InvoicereceiptsUpdateModel.

                - our_reference (str): our_reference of the InvoicereceiptsUpdateModel.

                - payments (str): payments of the InvoicereceiptsUpdateModel.

                - products (str): products of the InvoicereceiptsUpdateModel.

                - related_documents_notes (str): related_documents_notes of the InvoicereceiptsUpdateModel.

                - salesman_commission (str): salesman_commission of the InvoicereceiptsUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicereceiptsUpdateModel.

                - special_discount (str): special_discount of the InvoicereceiptsUpdateModel.

                - status (str): status of the InvoicereceiptsUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the InvoicereceiptsUpdateModel.

                - your_reference (str): your_reference of the InvoicereceiptsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicereceiptsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
