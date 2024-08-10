from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class Associated_documents(BaseModel):
    associated_id: Optional[Any] = None
    value: Optional[Any] = None


class Payments(BaseModel):
    date: Optional[Any] = None
    notes: Optional[Any] = None
    payment_method_id: Optional[Any] = None
    value: Optional[Any] = None


class Products(BaseModel):
    discount: Optional[Any] = None
    exemption_reason: Optional[Any] = None
    name: Optional[Any] = None
    order: Optional[Any] = None
    price: Optional[Any] = None
    product_id: Optional[Any] = None
    qty: Optional[Any] = None
    summary: Optional[Any] = None
    taxes: Optional[Any] = None
    warehouse_id: Optional[Any] = None


class SimplifiedinvoicesCountModel(BaseModel):
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


class SimplifiedinvoicesDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_id: Optional[Union[str, int]] = None


class SimplifiedinvoicesGetAllModel(BaseModel):
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


class SimplifiedinvoicesGetOneModel(BaseModel):
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


class SimplifiedinvoicesInsertModel(BaseModel):
    company_id: Union[str, int]
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
    payments: Optional[List[Payments]] = None
    products: Optional[List[Products]] = None
    related_documents_notes: Optional[str] = None
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    special_discount: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[Union[str, int]] = None
    your_reference: Optional[str] = None


class SimplifiedinvoicesUpdateModel(BaseModel):
    company_id: Union[str, int]
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
    payments: Optional[List[Payments]] = None
    products: Optional[List[Products]] = None
    related_documents_notes: Optional[str] = None
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    special_discount: Optional[str] = None
    status: Optional[str] = None
    vehicle_id: Optional[Union[str, int]] = None
    your_reference: Optional[str] = None


class SimplifiedinvoicesClient(MoloniBaseClient):

    @endpoint("/<version>/simplifiedInvoices/count/", method="post")
    def count(self, data: Union[SimplifiedinvoicesCountModel, dict], **kwargs):
        """
        count(self, data: Union[SimplifiedinvoicesCountModel, dict], **kwargs)

        Args:

            data (Union[SimplifiedinvoicesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SimplifiedinvoicesCountModel.

                - customer_id (Union[str, int]): customer_id of the SimplifiedinvoicesCountModel.

                - date (str): date of the SimplifiedinvoicesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the SimplifiedinvoicesCountModel.

                - expiration_date (str): expiration_date of the SimplifiedinvoicesCountModel.

                - number (str): number of the SimplifiedinvoicesCountModel.

                - our_reference (str): our_reference of the SimplifiedinvoicesCountModel.

                - salesman_id (Union[str, int]): salesman_id of the SimplifiedinvoicesCountModel.

                - supplier_id (Union[str, int]): supplier_id of the SimplifiedinvoicesCountModel.

                - year (str): year of the SimplifiedinvoicesCountModel.

                - your_reference (str): your_reference of the SimplifiedinvoicesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SimplifiedinvoicesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/simplifiedInvoices/delete/", method="post")
    def delete(self, data: Union[SimplifiedinvoicesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[SimplifiedinvoicesDeleteModel, dict], **kwargs)

        Args:

            data (Union[SimplifiedinvoicesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SimplifiedinvoicesDeleteModel.

                - document_id (Union[str, int]): document_id of the SimplifiedinvoicesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SimplifiedinvoicesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/simplifiedInvoices/getAll/", method="post")
    def get_all(self, data: Union[SimplifiedinvoicesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[SimplifiedinvoicesGetAllModel, dict], **kwargs)

        Args:

            data (Union[SimplifiedinvoicesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SimplifiedinvoicesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the SimplifiedinvoicesGetAllModel.

                - date (str): date of the SimplifiedinvoicesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the SimplifiedinvoicesGetAllModel.

                - expiration_date (str): expiration_date of the SimplifiedinvoicesGetAllModel.

                - number (str): number of the SimplifiedinvoicesGetAllModel.

                - offset (str): offset of the SimplifiedinvoicesGetAllModel.

                - our_reference (str): our_reference of the SimplifiedinvoicesGetAllModel.

                - qty (str): qty of the SimplifiedinvoicesGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the SimplifiedinvoicesGetAllModel.

                - supplier_id (Union[str, int]): supplier_id of the SimplifiedinvoicesGetAllModel.

                - year (str): year of the SimplifiedinvoicesGetAllModel.

                - your_reference (str): your_reference of the SimplifiedinvoicesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SimplifiedinvoicesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/simplifiedInvoices/getOne/", method="post")
    def get_one(self, data: Union[SimplifiedinvoicesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[SimplifiedinvoicesGetOneModel, dict], **kwargs)

        Args:

            data (Union[SimplifiedinvoicesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SimplifiedinvoicesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the SimplifiedinvoicesGetOneModel.

                - date (str): date of the SimplifiedinvoicesGetOneModel.

                - document_id (Union[str, int]): document_id of the SimplifiedinvoicesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the SimplifiedinvoicesGetOneModel.

                - expiration_date (str): expiration_date of the SimplifiedinvoicesGetOneModel.

                - number (str): number of the SimplifiedinvoicesGetOneModel.

                - our_reference (str): our_reference of the SimplifiedinvoicesGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the SimplifiedinvoicesGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the SimplifiedinvoicesGetOneModel.

                - year (str): year of the SimplifiedinvoicesGetOneModel.

                - your_reference (str): your_reference of the SimplifiedinvoicesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SimplifiedinvoicesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/simplifiedInvoices/insert/", method="post")
    def insert(self, data: Union[SimplifiedinvoicesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[SimplifiedinvoicesInsertModel, dict], **kwargs)

        Args:

            data (Union[SimplifiedinvoicesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the SimplifiedinvoicesInsertModel.

                - company_id (Union[str, int]): company_id of the SimplifiedinvoicesInsertModel.

                - customer_id (Union[str, int]): customer_id of the SimplifiedinvoicesInsertModel.

                - date (str): date of the SimplifiedinvoicesInsertModel.

                - deduction_id (Union[str, int]): deduction_id of the SimplifiedinvoicesInsertModel.

                - delivery_datetime (str): delivery_datetime of the SimplifiedinvoicesInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the SimplifiedinvoicesInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the SimplifiedinvoicesInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the SimplifiedinvoicesInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the SimplifiedinvoicesInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the SimplifiedinvoicesInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the SimplifiedinvoicesInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the SimplifiedinvoicesInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the SimplifiedinvoicesInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the SimplifiedinvoicesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the SimplifiedinvoicesInsertModel.

                - expiration_date (str): expiration_date of the SimplifiedinvoicesInsertModel.

                - financial_discount (str): financial_discount of the SimplifiedinvoicesInsertModel.

                - notes (str): notes of the SimplifiedinvoicesInsertModel.

                - our_reference (str): our_reference of the SimplifiedinvoicesInsertModel.

                - payments (str): payments of the SimplifiedinvoicesInsertModel.

                - products (str): products of the SimplifiedinvoicesInsertModel.

                - related_documents_notes (str): related_documents_notes of the SimplifiedinvoicesInsertModel.

                - salesman_commission (str): salesman_commission of the SimplifiedinvoicesInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the SimplifiedinvoicesInsertModel.

                - special_discount (str): special_discount of the SimplifiedinvoicesInsertModel.

                - status (str): status of the SimplifiedinvoicesInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the SimplifiedinvoicesInsertModel.

                - your_reference (str): your_reference of the SimplifiedinvoicesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SimplifiedinvoicesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/simplifiedInvoices/update/", method="post")
    def update(self, data: Union[SimplifiedinvoicesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[SimplifiedinvoicesUpdateModel, dict], **kwargs)

        Args:

            data (Union[SimplifiedinvoicesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the SimplifiedinvoicesUpdateModel.

                - company_id (Union[str, int]): company_id of the SimplifiedinvoicesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the SimplifiedinvoicesUpdateModel.

                - date (str): date of the SimplifiedinvoicesUpdateModel.

                - deduction_id (Union[str, int]): deduction_id of the SimplifiedinvoicesUpdateModel.

                - delivery_datetime (str): delivery_datetime of the SimplifiedinvoicesUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the SimplifiedinvoicesUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the SimplifiedinvoicesUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the SimplifiedinvoicesUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the SimplifiedinvoicesUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the SimplifiedinvoicesUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the SimplifiedinvoicesUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the SimplifiedinvoicesUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the SimplifiedinvoicesUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the SimplifiedinvoicesUpdateModel.

                - document_id (Union[str, int]): document_id of the SimplifiedinvoicesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the SimplifiedinvoicesUpdateModel.

                - expiration_date (str): expiration_date of the SimplifiedinvoicesUpdateModel.

                - financial_discount (str): financial_discount of the SimplifiedinvoicesUpdateModel.

                - notes (str): notes of the SimplifiedinvoicesUpdateModel.

                - our_reference (str): our_reference of the SimplifiedinvoicesUpdateModel.

                - payments (str): payments of the SimplifiedinvoicesUpdateModel.

                - products (str): products of the SimplifiedinvoicesUpdateModel.

                - related_documents_notes (str): related_documents_notes of the SimplifiedinvoicesUpdateModel.

                - salesman_commission (str): salesman_commission of the SimplifiedinvoicesUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the SimplifiedinvoicesUpdateModel.

                - special_discount (str): special_discount of the SimplifiedinvoicesUpdateModel.

                - status (str): status of the SimplifiedinvoicesUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the SimplifiedinvoicesUpdateModel.

                - your_reference (str): your_reference of the SimplifiedinvoicesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SimplifiedinvoicesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
