from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = ReceiptsClient(*args, **kwargs)
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


class ReceiptsCountModel(ApiRequestModel):
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


class ReceiptsDeleteModel(ApiRequestModel):
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


class ReceiptsGetAllModel(ApiRequestModel):
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


class ReceiptsGetOneModel(ApiRequestModel):
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


class ReceiptsInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    associated_documents: Optional[List[Associated_documents]] = None
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
    net_value: Optional[str] = None
    notes: Optional[str] = None
    payments: Optional[List[Payments]] = None
    related_documents_notes: Optional[str] = None
    status: Optional[str] = None

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


class ReceiptsUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    associated_documents: Optional[List[Associated_documents]] = None
    customer_id: Optional[Union[str, int]] = None
    date: Optional[str] = None
    document_id: Optional[Union[str, int]] = None
    document_set_id: Optional[Union[str, int]] = None
    net_value: Optional[str] = None
    notes: Optional[str] = None
    payments: Optional[List[Payments]] = None
    related_documents_notes: Optional[str] = None
    status: Optional[str] = None

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
