from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class EstimatesCountModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    salesman_id: Union[str, int]
    year: str
    your_reference: str


class EstimatesDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]


class EstimatesGetAllModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    offset: Union[str, int] = 0
    qty: Union[str, int] = 25
    salesman_id: Union[str, int]
    year: str
    your_reference: str


class EstimatesGetOneModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_id: Union[str, int]
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    salesman_id: Union[str, int]
    year: str
    your_reference: str


class EstimatesInsertModel(BaseModel):
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
    salesman_commission: str
    salesman_id: Union[str, int]
    special_discount: str
    status: str
    vehicle_id: Union[str, int]
    your_reference: str
    products: str = None


class EstimatesUpdateModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]
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
    products: str = None
    salesman_commission: str = None
    salesman_id: Union[str, int] = None
    special_discount: str = None
    status: str = None
    vehicle_id: Union[str, int] = None
    your_reference: str = None


class EstimatesClient(MoloniBaseClient):

    @endpoint("/<version>/estimates/count/", method="post")
    def count(self, data: Union[EstimatesCountModel, dict], **kwargs):
        """
        count(self, data: Union[EstimatesCountModel, dict], **kwargs)

        Args:

            data (Union[EstimatesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesCountModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesCountModel.

                - date (str): date of the EstimatesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesCountModel.

                - expiration_date (str): expiration_date of the EstimatesCountModel.

                - number (str): number of the EstimatesCountModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesCountModel.

                - year (str): year of the EstimatesCountModel.

                - your_reference (str): your_reference of the EstimatesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/delete/", method="post")
    def delete(self, data: Union[EstimatesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[EstimatesDeleteModel, dict], **kwargs)

        Args:

            data (Union[EstimatesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesDeleteModel.

                - document_id (Union[str, int]): document_id of the EstimatesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/getAll/", method="post")
    def get_all(self, data: Union[EstimatesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[EstimatesGetAllModel, dict], **kwargs)

        Args:

            data (Union[EstimatesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesGetAllModel.

                - date (str): date of the EstimatesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesGetAllModel.

                - expiration_date (str): expiration_date of the EstimatesGetAllModel.

                - number (str): number of the EstimatesGetAllModel.

                - offset (str): offset of the EstimatesGetAllModel.

                - qty (str): qty of the EstimatesGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesGetAllModel.

                - year (str): year of the EstimatesGetAllModel.

                - your_reference (str): your_reference of the EstimatesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/getOne/", method="post")
    def get_one(self, data: Union[EstimatesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[EstimatesGetOneModel, dict], **kwargs)

        Args:

            data (Union[EstimatesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesGetOneModel.

                - date (str): date of the EstimatesGetOneModel.

                - document_id (Union[str, int]): document_id of the EstimatesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesGetOneModel.

                - expiration_date (str): expiration_date of the EstimatesGetOneModel.

                - number (str): number of the EstimatesGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesGetOneModel.

                - year (str): year of the EstimatesGetOneModel.

                - your_reference (str): your_reference of the EstimatesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/insert/", method="post")
    def insert(self, data: Union[EstimatesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[EstimatesInsertModel, dict], **kwargs)

        Args:

            data (Union[EstimatesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesInsertModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesInsertModel.

                - date (str): date of the EstimatesInsertModel.

                - deduction_id (Union[str, int]): deduction_id of the EstimatesInsertModel.

                - delivery_datetime (str): delivery_datetime of the EstimatesInsertModel.

                - delivery_departure_address (str): delivery_departure_address of the EstimatesInsertModel.

                - delivery_departure_city (str): delivery_departure_city of the EstimatesInsertModel.

                - delivery_departure_country (str): delivery_departure_country of the EstimatesInsertModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the EstimatesInsertModel.

                - delivery_destination_address (str): delivery_destination_address of the EstimatesInsertModel.

                - delivery_destination_city (str): delivery_destination_city of the EstimatesInsertModel.

                - delivery_destination_country (str): delivery_destination_country of the EstimatesInsertModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the EstimatesInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the EstimatesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesInsertModel.

                - expiration_date (str): expiration_date of the EstimatesInsertModel.

                - financial_discount (str): financial_discount of the EstimatesInsertModel.

                - notes (str): notes of the EstimatesInsertModel.

                - products (str): products of the EstimatesInsertModel.

                - salesman_commission (str): salesman_commission of the EstimatesInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesInsertModel.

                - special_discount (str): special_discount of the EstimatesInsertModel.

                - status (str): status of the EstimatesInsertModel.

                - vehicle_id (Union[str, int]): vehicle_id of the EstimatesInsertModel.

                - your_reference (str): your_reference of the EstimatesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/estimates/update/", method="post")
    def update(self, data: Union[EstimatesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[EstimatesUpdateModel, dict], **kwargs)

        Args:

            data (Union[EstimatesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the EstimatesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the EstimatesUpdateModel.

                - date (str): date of the EstimatesUpdateModel.

                - deduction_id (Union[str, int]): deduction_id of the EstimatesUpdateModel.

                - delivery_datetime (str): delivery_datetime of the EstimatesUpdateModel.

                - delivery_departure_address (str): delivery_departure_address of the EstimatesUpdateModel.

                - delivery_departure_city (str): delivery_departure_city of the EstimatesUpdateModel.

                - delivery_departure_country (str): delivery_departure_country of the EstimatesUpdateModel.

                - delivery_departure_zip_code (str): delivery_departure_zip_code of the EstimatesUpdateModel.

                - delivery_destination_address (str): delivery_destination_address of the EstimatesUpdateModel.

                - delivery_destination_city (str): delivery_destination_city of the EstimatesUpdateModel.

                - delivery_destination_country (str): delivery_destination_country of the EstimatesUpdateModel.

                - delivery_destination_zip_code (str): delivery_destination_zip_code of the EstimatesUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the EstimatesUpdateModel.

                - document_id (Union[str, int]): document_id of the EstimatesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the EstimatesUpdateModel.

                - expiration_date (str): expiration_date of the EstimatesUpdateModel.

                - financial_discount (str): financial_discount of the EstimatesUpdateModel.

                - notes (str): notes of the EstimatesUpdateModel.

                - products (str): products of the EstimatesUpdateModel.

                - salesman_commission (str): salesman_commission of the EstimatesUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the EstimatesUpdateModel.

                - special_discount (str): special_discount of the EstimatesUpdateModel.

                - status (str): status of the EstimatesUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the EstimatesUpdateModel.

                - your_reference (str): your_reference of the EstimatesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, EstimatesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
