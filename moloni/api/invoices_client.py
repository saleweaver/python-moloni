from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class Associated_documents(BaseModel):
    associated_id: Optional[Union[str, int]]
    value: Optional[Union[str, int]]


class Payments(BaseModel):
    date: Optional[Union[str, int]]
    notes: Optional[Union[str, int]]
    payment_method_id: Optional[Union[str, int]]
    value: Optional[Union[str, int]]


class Products(BaseModel):
    discount: Optional[Union[str, int]]
    exemption_reason: Optional[Union[str, int]]
    name: Optional[Union[str, int]]
    order: Optional[Union[str, int]]
    price: Optional[Union[str, int]]
    product_id: Optional[Union[str, int]]
    qty: Optional[Union[str, int]]
    summary: Optional[Union[str, int]]
    taxes: Optional[Union[str, int]]
    warehouse_id: Optional[Union[str, int]]


class InvoicesCountModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    number: Optional[str] = None
    our_reference: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    supplier_id: Optional[Union[str, int]] = None
    year: Optional[str] = None
    your_reference: Optional[str] = None


class InvoicesDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_id: Optional[Union[str, int]] = None


class InvoicesGetAllModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    number: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    our_reference: Optional[str] = None
    qty: Optional[Union[str, int]] = 25
    salesman_id: Optional[Union[str, int]] = None
    supplier_id: Optional[Union[str, int]] = None
    year: Optional[str] = None
    your_reference: Optional[str] = None


class InvoicesGetOneModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    number: Optional[str] = None
    our_reference: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    supplier_id: Optional[Union[str, int]] = None
    year: Optional[str] = None
    your_reference: Optional[str] = None


class InvoicesInsertModel(BaseModel):
    company_id: Union[str, int]
    alternate_address_id: Optional[Union[str, int]] = None
    associated_documents: Optional[List[Associated_documents]] = None
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    deduction_id: Optional[Union[str, int]] = None
    delivery_datetime: Optional[str] = None
    delivery_departure_address: Optional[str] = None
    delivery_departure_city: Optional[str] = None
    delivery_departure_country: Optional[str] = None
    delivery_departure_zip_code: Optional[str] = None
    delivery_destination_address: Optional[str] = None
    delivery_destination_city: Optional[str] = None
    delivery_destination_country: Optional[str] = None
    delivery_destination_zip_code: Optional[str] = None
    delivery_method_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    financial_discount: Optional[str] = None
    notes: Optional[str] = None
    our_reference: Optional[str] = None
    products: Optional[List[Products]] = None
    related_documents_notes: Optional[str] = None
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    special_discount: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[Union[str, int]] = None
    your_reference: Optional[str] = None


class InvoicesUpdateModel(BaseModel):
    company_id: Union[str, int]
    alternate_address_id: Optional[Union[str, int]] = None
    associated_documents: Optional[List[Associated_documents]] = None
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    deduction_id: Optional[Union[str, int]] = None
    delivery_datetime: Optional[str] = None
    delivery_departure_address: Optional[str] = None
    delivery_departure_city: Optional[str] = None
    delivery_departure_country: Optional[str] = None
    delivery_departure_zip_code: Optional[str] = None
    delivery_destination_address: Optional[str] = None
    delivery_destination_city: Optional[str] = None
    delivery_destination_country: Optional[str] = None
    delivery_destination_zip_code: Optional[str] = None
    delivery_method_id: Optional[Union[str, int]] = None
    document_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    expiration_date: Optional[str] = None
    financial_discount: Optional[str] = None
    notes: Optional[str] = None
    our_reference: Optional[str] = None
    products: Optional[List[Products]] = None
    related_documents_notes: Optional[str] = None
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    special_discount: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[Union[str, int]] = None
    your_reference: Optional[str] = None


class InvoicesClient(MoloniBaseClient):

    @endpoint("/<version>/invoices/count/", method="post")
    def count(self, data: Union[InvoicesCountModel, dict], **kwargs):
        """
        count(self, data: Union[InvoicesCountModel, dict], **kwargs)

        Args:

            data (Union[InvoicesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the InvoicesCountModel.

                - customer_id (Union[str, int]): customer_id of the InvoicesCountModel.

                - date (str): date of the InvoicesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicesCountModel.

                - expiration_date (str): expiration_date of the InvoicesCountModel.

                - number (str): number of the InvoicesCountModel.

                - our_reference (str): our_reference of the InvoicesCountModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicesCountModel.

                - supplier_id (Union[str, int]): supplier_id of the InvoicesCountModel.

                - year (str): year of the InvoicesCountModel.

                - your_reference (str): your_reference of the InvoicesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoices/delete/", method="post")
    def delete(self, data: Union[InvoicesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[InvoicesDeleteModel, dict], **kwargs)

        Args:

            data (Union[InvoicesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the InvoicesDeleteModel.

                - document_id (Union[str, int]): document_id of the InvoicesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoices/getAll/", method="post")
    def get_all(self, data: Union[InvoicesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[InvoicesGetAllModel, dict], **kwargs)

        Args:

            data (Union[InvoicesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the InvoicesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the InvoicesGetAllModel.

                - date (str): date of the InvoicesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicesGetAllModel.

                - expiration_date (str): expiration_date of the InvoicesGetAllModel.

                - number (str): number of the InvoicesGetAllModel.

                - offset (str): offset of the InvoicesGetAllModel.

                - our_reference (str): our_reference of the InvoicesGetAllModel.

                - qty (str): qty of the InvoicesGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicesGetAllModel.

                - supplier_id (Union[str, int]): supplier_id of the InvoicesGetAllModel.

                - year (str): year of the InvoicesGetAllModel.

                - your_reference (str): your_reference of the InvoicesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoices/getOne/", method="post")
    def get_one(self, data: Union[InvoicesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[InvoicesGetOneModel, dict], **kwargs)

        Args:

            data (Union[InvoicesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the InvoicesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the InvoicesGetOneModel.

                - date (str): date of the InvoicesGetOneModel.

                - document_id (Union[str, int]): document_id of the InvoicesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicesGetOneModel.

                - expiration_date (str): expiration_date of the InvoicesGetOneModel.

                - number (str): number of the InvoicesGetOneModel.

                - our_reference (str): our_reference of the InvoicesGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicesGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the InvoicesGetOneModel.

                - year (str): year of the InvoicesGetOneModel.

                - your_reference (str): your_reference of the InvoicesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoices/insert/", method="post")
    def insert(self, data: Union[InvoicesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[InvoicesInsertModel, dict], **kwargs)

        Args:

            data (Union[InvoicesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - alternate_address_id (Union[str, int]): alternate_address_id of the InvoicesInsertModel.

                - associated_documents (str): associated_documents of the InvoicesInsertModel.

                - company_id (Union[str, int]): company_id of the InvoicesInsertModel.

                - customer_id (Union[str, int]): customer_id of the InvoicesInsertModel.

                - date (str): date of the InvoicesInsertModel.

                - deduction_id (Union[str, int]): deduction_id of the InvoicesInsertModel.

                - delivery_datetime (str): delivery_datetime of the InvoicesInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the InvoicesInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the InvoicesInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the InvoicesInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the InvoicesInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the InvoicesInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the InvoicesInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the InvoicesInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the InvoicesInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the InvoicesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicesInsertModel.

                - expiration_date (str): expiration_date of the InvoicesInsertModel.

                - financial_discount (str): financial_discount of the InvoicesInsertModel.

                - notes (str): notes of the InvoicesInsertModel.

                - our_reference (str): our_reference of the InvoicesInsertModel.

                - products (str): products of the InvoicesInsertModel.

                - related_documents_notes (str): related_documents_notes of the InvoicesInsertModel.

                - salesman_commission (str): salesman_commission of the InvoicesInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicesInsertModel.

                - special_discount (str): special_discount of the InvoicesInsertModel.

                - status (str): status of the InvoicesInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the InvoicesInsertModel.

                - your_reference (str): your_reference of the InvoicesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/invoices/update/", method="post")
    def update(self, data: Union[InvoicesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[InvoicesUpdateModel, dict], **kwargs)

        Args:

            data (Union[InvoicesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - alternate_address_id (Union[str, int]): alternate_address_id of the InvoicesUpdateModel.

                - associated_documents (str): associated_documents of the InvoicesUpdateModel.

                - company_id (Union[str, int]): company_id of the InvoicesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the InvoicesUpdateModel.

                - date (str): date of the InvoicesUpdateModel.

                - deduction_id (Union[str, int]): deduction_id of the InvoicesUpdateModel.

                - delivery_datetime (str): delivery_datetime of the InvoicesUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the InvoicesUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the InvoicesUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the InvoicesUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the InvoicesUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the InvoicesUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the InvoicesUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the InvoicesUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the InvoicesUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the InvoicesUpdateModel.

                - document_id (Union[str, int]): document_id of the InvoicesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the InvoicesUpdateModel.

                - expiration_date (str): expiration_date of the InvoicesUpdateModel.

                - financial_discount (str): financial_discount of the InvoicesUpdateModel.

                - notes (str): notes of the InvoicesUpdateModel.

                - our_reference (str): our_reference of the InvoicesUpdateModel.

                - products (str): products of the InvoicesUpdateModel.

                - related_documents_notes (str): related_documents_notes of the InvoicesUpdateModel.

                - salesman_commission (str): salesman_commission of the InvoicesUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the InvoicesUpdateModel.

                - special_discount (str): special_discount of the InvoicesUpdateModel.

                - status (str): status of the InvoicesUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the InvoicesUpdateModel.

                - your_reference (str): your_reference of the InvoicesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, InvoicesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
