from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class WaybillsCountModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    number: str
    year: str
    your_reference: str


class WaybillsDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]


class WaybillsGetAllModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    number: str
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25
    year: str
    your_reference: str


class WaybillsGetOneModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_id: Union[str, int]
    document_set_id: Union[str, int]
    number: str
    year: str
    your_reference: str


class WaybillsInsertModel(BaseModel):
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


class WaybillsSetTransportCodeModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]
    transport_code: str


class WaybillsUpdateModel(BaseModel):
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


class WaybillsClient(MoloniBaseClient):

    @endpoint("/<version>/waybills/count/", method="post")
    def count(self, data: Union[WaybillsCountModel, dict], **kwargs):
        """
        count(self, data: Union[WaybillsCountModel, dict], **kwargs)

        Args:

            data (Union[WaybillsCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsCountModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsCountModel.

                - date (str): date of the WaybillsCountModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsCountModel.

                - number (str): number of the WaybillsCountModel.

                - year (str): year of the WaybillsCountModel.

                - your_reference (str): your_reference of the WaybillsCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/delete/", method="post")
    def delete(self, data: Union[WaybillsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[WaybillsDeleteModel, dict], **kwargs)

        Args:

            data (Union[WaybillsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsDeleteModel.

                - document_id (Union[str, int]): document_id of the WaybillsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/getAll/", method="post")
    def get_all(self, data: Union[WaybillsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[WaybillsGetAllModel, dict], **kwargs)

        Args:

            data (Union[WaybillsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsGetAllModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsGetAllModel.

                - date (str): date of the WaybillsGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsGetAllModel.

                - number (str): number of the WaybillsGetAllModel.

                - offset (str): offset of the WaybillsGetAllModel.

                - qty (str): qty of the WaybillsGetAllModel.

                - year (str): year of the WaybillsGetAllModel.

                - your_reference (str): your_reference of the WaybillsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/getOne/", method="post")
    def get_one(self, data: Union[WaybillsGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[WaybillsGetOneModel, dict], **kwargs)

        Args:

            data (Union[WaybillsGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsGetOneModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsGetOneModel.

                - date (str): date of the WaybillsGetOneModel.

                - document_id (Union[str, int]): document_id of the WaybillsGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsGetOneModel.

                - number (str): number of the WaybillsGetOneModel.

                - year (str): year of the WaybillsGetOneModel.

                - your_reference (str): your_reference of the WaybillsGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/insert/", method="post")
    def insert(self, data: Union[WaybillsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[WaybillsInsertModel, dict], **kwargs)

        Args:

            data (Union[WaybillsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the WaybillsInsertModel.

                - company_id (Union[str, int]): company_id of the WaybillsInsertModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsInsertModel.

                - date (str): date of the WaybillsInsertModel.

                - delivery_datetime (str): delivery_datetime of the WaybillsInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the WaybillsInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the WaybillsInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the WaybillsInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the WaybillsInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the WaybillsInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the WaybillsInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the WaybillsInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the WaybillsInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the WaybillsInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsInsertModel.

                - financial_discount (str): financial_discount of the WaybillsInsertModel.

                - notes (str): notes of the WaybillsInsertModel.

                - products (str): products of the WaybillsInsertModel.

                - related_documents_notes (str): related_documents_notes of the WaybillsInsertModel.

                - status (str): status of the WaybillsInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the WaybillsInsertModel.

                - your_reference (str): your_reference of the WaybillsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/setTransportCode/", method="post")
    def set_transport_code(
        self, data: Union[WaybillsSetTransportCodeModel, dict], **kwargs
    ):
        """
        set_transport_code(self, data: Union[WaybillsSetTransportCodeModel, dict], **kwargs)

        Args:

            data (Union[WaybillsSetTransportCodeModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the WaybillsSetTransportCodeModel.

                - document_id (Union[str, int]): document_id of the WaybillsSetTransportCodeModel.

                - transport_code (str): transport_code of the WaybillsSetTransportCodeModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsSetTransportCodeModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/waybills/update/", method="post")
    def update(self, data: Union[WaybillsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[WaybillsUpdateModel, dict], **kwargs)

        Args:

            data (Union[WaybillsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the WaybillsUpdateModel.

                - company_id (Union[str, int]): company_id of the WaybillsUpdateModel.

                - customer_id (Union[str, int]): customer_id of the WaybillsUpdateModel.

                - date (str): date of the WaybillsUpdateModel.

                - delivery_datetime (str): delivery_datetime of the WaybillsUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the WaybillsUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the WaybillsUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the WaybillsUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the WaybillsUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the WaybillsUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the WaybillsUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the WaybillsUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the WaybillsUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the WaybillsUpdateModel.

                - document_id (Union[str, int]): document_id of the WaybillsUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the WaybillsUpdateModel.

                - financial_discount (str): financial_discount of the WaybillsUpdateModel.

                - notes (str): notes of the WaybillsUpdateModel.

                - products (str): products of the WaybillsUpdateModel.

                - related_documents_notes (str): related_documents_notes of the WaybillsUpdateModel.

                - status (str): status of the WaybillsUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the WaybillsUpdateModel.

                - your_reference (str): your_reference of the WaybillsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, WaybillsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
