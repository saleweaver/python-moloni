from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = CreditnotesClient(*args, **kwargs)
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


class CreditnotesCountModel(ApiRequestModel):
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


class CreditnotesDeleteModel(ApiRequestModel):
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


class CreditnotesGetAllModel(ApiRequestModel):
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


class CreditnotesGetOneModel(ApiRequestModel):
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


class CreditnotesInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    associated_documents: Optional[List[Associated_documents]] = None
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    deduction_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    financial_discount: Optional[str] = None
    notes: Optional[str] = None
    products: Optional[List[Products]] = None
    related_documents_notes: Optional[str] = None
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    status: Optional[str] = None
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


class CreditnotesUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    associated_documents: Optional[List[Associated_documents]] = None
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    deduction_id: Optional[Union[str, int]] = None
    document_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    financial_discount: Optional[str] = None
    notes: Optional[str] = None
    products: Optional[List[Products]] = None
    related_documents_notes: Optional[str] = None
    salesman_commission: Optional[str] = None
    salesman_id: Optional[Union[str, int]] = None
    status: Optional[str] = None
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


class CreditnotesClient(MoloniBaseClient):

    @endpoint("/<version>/creditNotes/count/", method="post")
    def count(self, data: Union[CreditnotesCountModel, dict], **kwargs):
        """
        count(self, data: Union[CreditnotesCountModel, dict], **kwargs)

        Args:

            data (Union[CreditnotesCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CreditnotesCountModel.

                - customer_id (Union[str, int]): customer_id of the CreditnotesCountModel.

                - date (str): date of the CreditnotesCountModel.

                - document_set_id (Union[str, int]): document_set_id of the CreditnotesCountModel.

                - expiration_date (str): expiration_date of the CreditnotesCountModel.

                - number (str): number of the CreditnotesCountModel.

                - our_reference (str): our_reference of the CreditnotesCountModel.

                - salesman_id (Union[str, int]): salesman_id of the CreditnotesCountModel.

                - supplier_id (Union[str, int]): supplier_id of the CreditnotesCountModel.

                - year (str): year of the CreditnotesCountModel.

                - your_reference (str): your_reference of the CreditnotesCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CreditnotesCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/creditNotes/delete/", method="post")
    def delete(self, data: Union[CreditnotesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[CreditnotesDeleteModel, dict], **kwargs)

        Args:

            data (Union[CreditnotesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CreditnotesDeleteModel.

                - document_id (Union[str, int]): document_id of the CreditnotesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CreditnotesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/creditNotes/getAll/", method="post")
    def get_all(self, data: Union[CreditnotesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[CreditnotesGetAllModel, dict], **kwargs)

        Args:

            data (Union[CreditnotesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CreditnotesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the CreditnotesGetAllModel.

                - date (str): date of the CreditnotesGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the CreditnotesGetAllModel.

                - expiration_date (str): expiration_date of the CreditnotesGetAllModel.

                - number (str): number of the CreditnotesGetAllModel.

                - offset (str): offset of the CreditnotesGetAllModel.

                - our_reference (str): our_reference of the CreditnotesGetAllModel.

                - qty (str): qty of the CreditnotesGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the CreditnotesGetAllModel.

                - supplier_id (Union[str, int]): supplier_id of the CreditnotesGetAllModel.

                - year (str): year of the CreditnotesGetAllModel.

                - your_reference (str): your_reference of the CreditnotesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CreditnotesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/creditNotes/getOne/", method="post")
    def get_one(self, data: Union[CreditnotesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[CreditnotesGetOneModel, dict], **kwargs)

        Args:

            data (Union[CreditnotesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CreditnotesGetOneModel.

                - customer_id (Union[str, int]): customer_id of the CreditnotesGetOneModel.

                - date (str): date of the CreditnotesGetOneModel.

                - document_id (Union[str, int]): document_id of the CreditnotesGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the CreditnotesGetOneModel.

                - expiration_date (str): expiration_date of the CreditnotesGetOneModel.

                - number (str): number of the CreditnotesGetOneModel.

                - our_reference (str): our_reference of the CreditnotesGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the CreditnotesGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the CreditnotesGetOneModel.

                - year (str): year of the CreditnotesGetOneModel.

                - your_reference (str): your_reference of the CreditnotesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CreditnotesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/creditNotes/insert/", method="post")
    def insert(self, data: Union[CreditnotesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[CreditnotesInsertModel, dict], **kwargs)

        Args:

            data (Union[CreditnotesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the CreditnotesInsertModel.

                - company_id (Union[str, int]): company_id of the CreditnotesInsertModel.

                - customer_id (Union[str, int]): customer_id of the CreditnotesInsertModel.

                - date (str): date of the CreditnotesInsertModel.

                - deduction_id (Union[str, int]): deduction_id of the CreditnotesInsertModel.

                - document_set_id (Union[str, int]): document_set_id of the CreditnotesInsertModel.

                - financial_discount (str): financial_discount of the CreditnotesInsertModel.

                - notes (str): notes of the CreditnotesInsertModel.

                - products (str): products of the CreditnotesInsertModel.

                - related_documents_notes (str): related_documents_notes of the CreditnotesInsertModel.

                - salesman_commission (str): salesman_commission of the CreditnotesInsertModel.

                - salesman_id (Union[str, int]): salesman_id of the CreditnotesInsertModel.

                - status (str): status of the CreditnotesInsertModel.

                - your_reference (str): your_reference of the CreditnotesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CreditnotesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/creditNotes/update/", method="post")
    def update(self, data: Union[CreditnotesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[CreditnotesUpdateModel, dict], **kwargs)

        Args:

            data (Union[CreditnotesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - associated_documents (str): associated_documents of the CreditnotesUpdateModel.

                - company_id (Union[str, int]): company_id of the CreditnotesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the CreditnotesUpdateModel.

                - date (str): date of the CreditnotesUpdateModel.

                - deduction_id (Union[str, int]): deduction_id of the CreditnotesUpdateModel.

                - document_id (Union[str, int]): document_id of the CreditnotesUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the CreditnotesUpdateModel.

                - financial_discount (str): financial_discount of the CreditnotesUpdateModel.

                - notes (str): notes of the CreditnotesUpdateModel.

                - products (str): products of the CreditnotesUpdateModel.

                - related_documents_notes (str): related_documents_notes of the CreditnotesUpdateModel.

                - salesman_commission (str): salesman_commission of the CreditnotesUpdateModel.

                - salesman_id (Union[str, int]): salesman_id of the CreditnotesUpdateModel.

                - status (str): status of the CreditnotesUpdateModel.

                - your_reference (str): your_reference of the CreditnotesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CreditnotesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
