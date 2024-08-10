from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class CustomerreturnnotesCountModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    number: str
    year: str
    your_reference: str


class CustomerreturnnotesDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]


class CustomerreturnnotesGetAllModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    number: str
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25
    year: str
    your_reference: str


class CustomerreturnnotesGetOneModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_id: Union[str, int]
    document_set_id: Union[str, int]
    number: str
    year: str
    your_reference: str


class CustomerreturnnotesInsertModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
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
    financial_discount: str
    notes: str
    related_documents_notes: str
    status: str
    vehicle_id: Union[str, int]
    your_reference: str
    associated_documents: str = None
    products: str = None


class CustomerreturnnotesSetTransportCodeModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]
    transport_code: str


class CustomerreturnnotesUpdateModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]
    associated_documents: str = None
    customer_id: Union[str, int] = None
    date: str = None
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
    financial_discount: str = None
    notes: str = None
    products: str = None
    related_documents_notes: str = None
    status: str = None
    vehicle_id: Union[str, int] = None
    your_reference: str = None


class CustomerreturnnotesClient(MoloniBaseClient):

    @endpoint("/<version>/customerReturnNotes/count/", method="post")
    def count(self, data: Union[CustomerreturnnotesCountModel, dict], **kwargs):
        """
        count(self, data: Union[CustomerreturnnotesCountModel, dict], **kwargs)

        Args:

            data (Union[CustomerreturnnotesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomerreturnnotesCountModel.

                - customer_id (Union[str, int]): customer_id of the CustomerreturnnotesCountModel.

                - date (str): date of the CustomerreturnnotesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the CustomerreturnnotesCountModel.

                - number (str): number of the CustomerreturnnotesCountModel.

                - year (str): year of the CustomerreturnnotesCountModel.

                - your_reference (str): your_reference of the CustomerreturnnotesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomerreturnnotesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerReturnNotes/delete/", method="post")
    def delete(self, data: Union[CustomerreturnnotesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[CustomerreturnnotesDeleteModel, dict], **kwargs)

        Args:

            data (Union[CustomerreturnnotesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomerreturnnotesDeleteModel.

                - document_id (Union[str, int]): document_id of the CustomerreturnnotesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomerreturnnotesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerReturnNotes/getAll/", method="post")
    def get_all(self, data: Union[CustomerreturnnotesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[CustomerreturnnotesGetAllModel, dict], **kwargs)

        Args:

            data (Union[CustomerreturnnotesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomerreturnnotesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the CustomerreturnnotesGetAllModel.

                - date (str): date of the CustomerreturnnotesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the CustomerreturnnotesGetAllModel.

                - number (str): number of the CustomerreturnnotesGetAllModel.

                - offset (str): offset of the CustomerreturnnotesGetAllModel.

                - qty (str): qty of the CustomerreturnnotesGetAllModel.

                - year (str): year of the CustomerreturnnotesGetAllModel.

                - your_reference (str): your_reference of the CustomerreturnnotesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomerreturnnotesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerReturnNotes/getOne/", method="post")
    def get_one(self, data: Union[CustomerreturnnotesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[CustomerreturnnotesGetOneModel, dict], **kwargs)

        Args:

            data (Union[CustomerreturnnotesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomerreturnnotesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the CustomerreturnnotesGetOneModel.

                - date (str): date of the CustomerreturnnotesGetOneModel.

                - document_id (Union[str, int]): document_id of the CustomerreturnnotesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the CustomerreturnnotesGetOneModel.

                - number (str): number of the CustomerreturnnotesGetOneModel.

                - year (str): year of the CustomerreturnnotesGetOneModel.

                - your_reference (str): your_reference of the CustomerreturnnotesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomerreturnnotesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerReturnNotes/insert/", method="post")
    def insert(self, data: Union[CustomerreturnnotesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[CustomerreturnnotesInsertModel, dict], **kwargs)

        Args:

            data (Union[CustomerreturnnotesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the CustomerreturnnotesInsertModel.

                - company_id (Union[str, int]): company_id of the CustomerreturnnotesInsertModel.

                - customer_id (Union[str, int]): customer_id of the CustomerreturnnotesInsertModel.

                - date (str): date of the CustomerreturnnotesInsertModel.

                - delivery_datetime (str): delivery_datetime of the CustomerreturnnotesInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the CustomerreturnnotesInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the CustomerreturnnotesInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the CustomerreturnnotesInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the CustomerreturnnotesInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the CustomerreturnnotesInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the CustomerreturnnotesInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the CustomerreturnnotesInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the CustomerreturnnotesInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the CustomerreturnnotesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the CustomerreturnnotesInsertModel.

                - financial_discount (str): financial_discount of the CustomerreturnnotesInsertModel.

                - notes (str): notes of the CustomerreturnnotesInsertModel.

                - products (str): products of the CustomerreturnnotesInsertModel.

                - related_documents_notes (str): related_documents_notes of the CustomerreturnnotesInsertModel.

                - status (str): status of the CustomerreturnnotesInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the CustomerreturnnotesInsertModel.

                - your_reference (str): your_reference of the CustomerreturnnotesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomerreturnnotesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerReturnNotes/setTransportCode/", method="post")
    def set_transport_code(
        self, data: Union[CustomerreturnnotesSetTransportCodeModel, dict], **kwargs
    ):
        """
        set_transport_code(self, data: Union[CustomerreturnnotesSetTransportCodeModel, dict], **kwargs)

        Args:

            data (Union[CustomerreturnnotesSetTransportCodeModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomerreturnnotesSetTransportCodeModel.

                - document_id (Union[str, int]): document_id of the CustomerreturnnotesSetTransportCodeModel.

                - transport_code (str): transport_code of the CustomerreturnnotesSetTransportCodeModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, CustomerreturnnotesSetTransportCodeModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerReturnNotes/update/", method="post")
    def update(self, data: Union[CustomerreturnnotesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[CustomerreturnnotesUpdateModel, dict], **kwargs)

        Args:

            data (Union[CustomerreturnnotesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the CustomerreturnnotesUpdateModel.

                - company_id (Union[str, int]): company_id of the CustomerreturnnotesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the CustomerreturnnotesUpdateModel.

                - date (str): date of the CustomerreturnnotesUpdateModel.

                - delivery_datetime (str): delivery_datetime of the CustomerreturnnotesUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the CustomerreturnnotesUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the CustomerreturnnotesUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the CustomerreturnnotesUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the CustomerreturnnotesUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the CustomerreturnnotesUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the CustomerreturnnotesUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the CustomerreturnnotesUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the CustomerreturnnotesUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the CustomerreturnnotesUpdateModel.

                - document_id (Union[str, int]): document_id of the CustomerreturnnotesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the CustomerreturnnotesUpdateModel.

                - financial_discount (str): financial_discount of the CustomerreturnnotesUpdateModel.

                - notes (str): notes of the CustomerreturnnotesUpdateModel.

                - products (str): products of the CustomerreturnnotesUpdateModel.

                - related_documents_notes (str): related_documents_notes of the CustomerreturnnotesUpdateModel.

                - status (str): status of the CustomerreturnnotesUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the CustomerreturnnotesUpdateModel.

                - your_reference (str): your_reference of the CustomerreturnnotesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomerreturnnotesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
