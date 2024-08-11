from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = InvoicereceiptsClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        pass


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


class InvoicereceiptsCountModel(ApiRequestModel):
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

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.count(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class InvoicereceiptsDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    document_id: Optional[Union[str, int]] = None

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.delete(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class InvoicereceiptsGetAllModel(ApiRequestModel):
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

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.get_all(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class InvoicereceiptsGetOneModel(ApiRequestModel):
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

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.get_one(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class InvoicereceiptsInsertModel(ApiRequestModel):
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

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.insert(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class InvoicereceiptsUpdateModel(ApiRequestModel):
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

    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse

        Make an API request using the initialized client.

        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method).
        If the client is initialized, it will make an API request using the provided method name and the model's data,
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.

        Returns:
            The response from the API.

        Raises:
            ValueError: If the client is not initialized via the `connect` method.

        Example:

                # Assuming you have a model instance `request_model` and an API client `api_client`

                ..code-block:: python

                    with request_model.connect(auth_config=auth_config) as api:
                        response = api.request()

                # The above example assumes that the `connect` method has been used to initialize the client.
                # The request method then sends the model's data to the API and returns the API's response.

        """
        if hasattr(self, "_api_client"):
            response = self._api_client.update(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


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
