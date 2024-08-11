from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = DocumentsClient(*args, **kwargs)
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


class DocumentsCountModel(ApiRequestModel):
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


class DocumentsGetAllModel(ApiRequestModel):
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


class DocumentsGetAllDocumentTypesModel(ApiRequestModel):
    language_id: Optional[Union[str, int]] = None

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
            response = self._api_client.get_all_document_types(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DocumentsGetOneModel(ApiRequestModel):
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


class DocumentsGetPdfLinkModel(ApiRequestModel):
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
            response = self._api_client.get_pdf_link(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class DocumentsClient(MoloniBaseClient):

    @endpoint("/<version>/documents/count/", method="post")
    def count(self, data: Union[DocumentsCountModel, dict], **kwargs):
        """
        count(self, data: Union[DocumentsCountModel, dict], **kwargs)

        Args:

            data (Union[DocumentsCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsCountModel.

                - customer_id (Union[str, int]): customer_id of the DocumentsCountModel.

                - date (str): date of the DocumentsCountModel.

                - document_set_id (Union[str, int]): document_set_id of the DocumentsCountModel.

                - expiration_date (str): expiration_date of the DocumentsCountModel.

                - number (str): number of the DocumentsCountModel.

                - our_reference (str): our_reference of the DocumentsCountModel.

                - salesman_id (Union[str, int]): salesman_id of the DocumentsCountModel.

                - supplier_id (Union[str, int]): supplier_id of the DocumentsCountModel.

                - year (str): year of the DocumentsCountModel.

                - your_reference (str): your_reference of the DocumentsCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documents/getAll/", method="post")
    def get_all(self, data: Union[DocumentsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[DocumentsGetAllModel, dict], **kwargs)

        Args:

            data (Union[DocumentsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsGetAllModel.

                - customer_id (Union[str, int]): customer_id of the DocumentsGetAllModel.

                - date (str): date of the DocumentsGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the DocumentsGetAllModel.

                - expiration_date (str): expiration_date of the DocumentsGetAllModel.

                - number (str): number of the DocumentsGetAllModel.

                - offset (str): offset of the DocumentsGetAllModel.

                - our_reference (str): our_reference of the DocumentsGetAllModel.

                - qty (str): qty of the DocumentsGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the DocumentsGetAllModel.

                - supplier_id (Union[str, int]): supplier_id of the DocumentsGetAllModel.

                - year (str): year of the DocumentsGetAllModel.

                - your_reference (str): your_reference of the DocumentsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documents/getAllDocumentTypes/", method="post")
    def get_all_document_types(
        self, data: Union[DocumentsGetAllDocumentTypesModel, dict], **kwargs
    ):
        """
        get_all_document_types(self, data: Union[DocumentsGetAllDocumentTypesModel, dict], **kwargs)

        Args:

            data (Union[DocumentsGetAllDocumentTypesModel, dict]): A model instance or dictionary containing the following fields:

                - language_id (Union[str, int]): language_id of the DocumentsGetAllDocumentTypesModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsGetAllDocumentTypesModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documents/getOne/", method="post")
    def get_one(self, data: Union[DocumentsGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[DocumentsGetOneModel, dict], **kwargs)

        Args:

            data (Union[DocumentsGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsGetOneModel.

                - customer_id (Union[str, int]): customer_id of the DocumentsGetOneModel.

                - date (str): date of the DocumentsGetOneModel.

                - document_id (Union[str, int]): document_id of the DocumentsGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the DocumentsGetOneModel.

                - expiration_date (str): expiration_date of the DocumentsGetOneModel.

                - number (str): number of the DocumentsGetOneModel.

                - our_reference (str): our_reference of the DocumentsGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the DocumentsGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the DocumentsGetOneModel.

                - year (str): year of the DocumentsGetOneModel.

                - your_reference (str): your_reference of the DocumentsGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documents/getPDFLink/", method="post")
    def get_pdf_link(self, data: Union[DocumentsGetPdfLinkModel, dict], **kwargs):
        """
        get_pdf_link(self, data: Union[DocumentsGetPdfLinkModel, dict], **kwargs)

        Args:

            data (Union[DocumentsGetPdfLinkModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsGetPdfLinkModel.

                - document_id (Union[str, int]): document_id of the DocumentsGetPdfLinkModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsGetPdfLinkModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
