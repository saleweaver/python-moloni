from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = SuppliersClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class SuppliersCountModel(ApiRequestModel):
    company_id: Union[str, int]

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


class SuppliersCountByNameModel(ApiRequestModel):
    company_id: Union[str, int]
    name: Optional[str] = None

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
            response = self._api_client.count_by_name(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersCountByNumberModel(ApiRequestModel):
    company_id: Union[str, int]
    number: Optional[str] = None

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
            response = self._api_client.count_by_number(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersCountBySearchModel(ApiRequestModel):
    company_id: Union[str, int]
    search: Optional[str] = None

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
            response = self._api_client.count_by_search(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersCountByVatModel(ApiRequestModel):
    company_id: Union[str, int]
    vat: Optional[str] = None

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
            response = self._api_client.count_by_vat(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersCountModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

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
            response = self._api_client.count_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    supplier_id: Optional[Union[str, int]] = None

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


class SuppliersGetAllModel(ApiRequestModel):
    company_id: Union[str, int]
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25

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


class SuppliersGetByNameModel(ApiRequestModel):
    company_id: Union[str, int]
    name: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25

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
            response = self._api_client.get_by_name(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersGetByNumberModel(ApiRequestModel):
    company_id: Union[str, int]
    number: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25

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
            response = self._api_client.get_by_number(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersGetBySearchModel(ApiRequestModel):
    company_id: Union[str, int]
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25
    search: Optional[str] = None

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
            response = self._api_client.get_by_search(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersGetByVatModel(ApiRequestModel):
    company_id: Union[str, int]
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25
    vat: Optional[str] = None

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
            response = self._api_client.get_by_vat(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersGetModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25

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
            response = self._api_client.get_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class SuppliersGetOneModel(ApiRequestModel):
    company_id: Union[str, int]
    supplier_id: Optional[Union[str, int]] = None

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


class SuppliersInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    city: Optional[str] = None
    contact_email: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    credit_limit: Optional[str] = None
    delivery_method_id: Optional[Union[str, int]] = None
    discount: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    field_notes: Optional[str] = None
    language_id: Optional[Union[str, int]] = None
    maturity_date_id: Optional[Union[str, int]] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    number: Optional[str] = None
    payment_method_id: Optional[Union[str, int]] = None
    phone: Optional[str] = None
    qty_copies_document: Optional[str] = None
    vat: Optional[str] = None
    website: Optional[str] = None
    zip_code: Optional[str] = None

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


class SuppliersUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    city: Optional[str] = None
    contact_email: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    credit_limit: Optional[str] = None
    delivery_method_id: Optional[Union[str, int]] = None
    discount: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    field_notes: Optional[str] = None
    language_id: Optional[Union[str, int]] = None
    maturity_date_id: Optional[Union[str, int]] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    number: Optional[str] = None
    payment_method_id: Optional[Union[str, int]] = None
    phone: Optional[str] = None
    qty_copies_document: Optional[str] = None
    supplier_id: Optional[Union[str, int]] = None
    vat: Optional[str] = None
    website: Optional[str] = None
    zip_code: Optional[str] = None

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


class SuppliersClient(MoloniBaseClient):

    @endpoint("/<version>/suppliers/count/", method="post")
    def count(self, data: Union[SuppliersCountModel, dict], **kwargs):
        """
        count(self, data: Union[SuppliersCountModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countByName/", method="post")
    def count_by_name(self, data: Union[SuppliersCountByNameModel, dict], **kwargs):
        """
        count_by_name(self, data: Union[SuppliersCountByNameModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountByNameModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountByNameModel.

                - name (str): name of the SuppliersCountByNameModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountByNameModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countByNumber/", method="post")
    def count_by_number(self, data: Union[SuppliersCountByNumberModel, dict], **kwargs):
        """
        count_by_number(self, data: Union[SuppliersCountByNumberModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountByNumberModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountByNumberModel.

                - number (str): number of the SuppliersCountByNumberModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountByNumberModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countBySearch/", method="post")
    def count_by_search(self, data: Union[SuppliersCountBySearchModel, dict], **kwargs):
        """
        count_by_search(self, data: Union[SuppliersCountBySearchModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountBySearchModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountBySearchModel.

                - search (str): search of the SuppliersCountBySearchModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountBySearchModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countByVat/", method="post")
    def count_by_vat(self, data: Union[SuppliersCountByVatModel, dict], **kwargs):
        """
        count_by_vat(self, data: Union[SuppliersCountByVatModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountByVatModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountByVatModel.

                - vat (str): vat of the SuppliersCountByVatModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountByVatModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[SuppliersCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[SuppliersCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[SuppliersCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the SuppliersCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/delete/", method="post")
    def delete(self, data: Union[SuppliersDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[SuppliersDeleteModel, dict], **kwargs)

        Args:

            data (Union[SuppliersDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersDeleteModel.

                - supplier_id (Union[str, int]): supplier_id of the SuppliersDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getAll/", method="post")
    def get_all(self, data: Union[SuppliersGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[SuppliersGetAllModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetAllModel.

                - offset (str): offset of the SuppliersGetAllModel.

                - qty (str): qty of the SuppliersGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getByName/", method="post")
    def get_by_name(self, data: Union[SuppliersGetByNameModel, dict], **kwargs):
        """
        get_by_name(self, data: Union[SuppliersGetByNameModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetByNameModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetByNameModel.

                - name (str): name of the SuppliersGetByNameModel.

                - offset (str): offset of the SuppliersGetByNameModel.

                - qty (str): qty of the SuppliersGetByNameModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetByNameModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getByNumber/", method="post")
    def get_by_number(self, data: Union[SuppliersGetByNumberModel, dict], **kwargs):
        """
        get_by_number(self, data: Union[SuppliersGetByNumberModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetByNumberModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetByNumberModel.

                - number (str): number of the SuppliersGetByNumberModel.

                - offset (str): offset of the SuppliersGetByNumberModel.

                - qty (str): qty of the SuppliersGetByNumberModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetByNumberModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getBySearch/", method="post")
    def get_by_search(self, data: Union[SuppliersGetBySearchModel, dict], **kwargs):
        """
        get_by_search(self, data: Union[SuppliersGetBySearchModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetBySearchModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetBySearchModel.

                - offset (str): offset of the SuppliersGetBySearchModel.

                - qty (str): qty of the SuppliersGetBySearchModel.

                - search (str): search of the SuppliersGetBySearchModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetBySearchModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getByVat/", method="post")
    def get_by_vat(self, data: Union[SuppliersGetByVatModel, dict], **kwargs):
        """
        get_by_vat(self, data: Union[SuppliersGetByVatModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetByVatModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetByVatModel.

                - offset (str): offset of the SuppliersGetByVatModel.

                - qty (str): qty of the SuppliersGetByVatModel.

                - vat (str): vat of the SuppliersGetByVatModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetByVatModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[SuppliersGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[SuppliersGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the SuppliersGetModifiedSinceModel.

                - offset (str): offset of the SuppliersGetModifiedSinceModel.

                - qty (str): qty of the SuppliersGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/getOne/", method="post")
    def get_one(self, data: Union[SuppliersGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[SuppliersGetOneModel, dict], **kwargs)

        Args:

            data (Union[SuppliersGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SuppliersGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the SuppliersGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/insert/", method="post")
    def insert(self, data: Union[SuppliersInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[SuppliersInsertModel, dict], **kwargs)

        Args:

            data (Union[SuppliersInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the SuppliersInsertModel.

                - city (str): city of the SuppliersInsertModel.

                - company_id (Union[str, int]): company_id of the SuppliersInsertModel.

                - contact_email (str): contact_email of the SuppliersInsertModel.

                - contact_name (str): contact_name of the SuppliersInsertModel.

                - contact_phone (str): contact_phone of the SuppliersInsertModel.

                - country_id (Union[str, int]): country_id of the SuppliersInsertModel.

                - credit_limit (str): credit_limit of the SuppliersInsertModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the SuppliersInsertModel.

                - discount (str): discount of the SuppliersInsertModel.

                - email (str): email of the SuppliersInsertModel.

                - fax (str): fax of the SuppliersInsertModel.

                - field_notes (str): field_notes of the SuppliersInsertModel.

                - language_id (Union[str, int]): language_id of the SuppliersInsertModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the SuppliersInsertModel.

                - name (str): name of the SuppliersInsertModel.

                - notes (str): notes of the SuppliersInsertModel.

                - number (str): number of the SuppliersInsertModel.

                - payment_method_id (Union[str, int]): payment_method_id of the SuppliersInsertModel.

                - phone (str): phone of the SuppliersInsertModel.

                - qty_copies_document (str): qty_copies_document of the SuppliersInsertModel.

                - vat (str): vat of the SuppliersInsertModel.

                - website (str): website of the SuppliersInsertModel.

                - zip_code (str): zip_code of the SuppliersInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/suppliers/update/", method="post")
    def update(self, data: Union[SuppliersUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[SuppliersUpdateModel, dict], **kwargs)

        Args:

            data (Union[SuppliersUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the SuppliersUpdateModel.

                - city (str): city of the SuppliersUpdateModel.

                - company_id (Union[str, int]): company_id of the SuppliersUpdateModel.

                - contact_email (str): contact_email of the SuppliersUpdateModel.

                - contact_name (str): contact_name of the SuppliersUpdateModel.

                - contact_phone (str): contact_phone of the SuppliersUpdateModel.

                - country_id (Union[str, int]): country_id of the SuppliersUpdateModel.

                - credit_limit (str): credit_limit of the SuppliersUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the SuppliersUpdateModel.

                - discount (str): discount of the SuppliersUpdateModel.

                - email (str): email of the SuppliersUpdateModel.

                - fax (str): fax of the SuppliersUpdateModel.

                - field_notes (str): field_notes of the SuppliersUpdateModel.

                - language_id (Union[str, int]): language_id of the SuppliersUpdateModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the SuppliersUpdateModel.

                - name (str): name of the SuppliersUpdateModel.

                - notes (str): notes of the SuppliersUpdateModel.

                - number (str): number of the SuppliersUpdateModel.

                - payment_method_id (Union[str, int]): payment_method_id of the SuppliersUpdateModel.

                - phone (str): phone of the SuppliersUpdateModel.

                - qty_copies_document (str): qty_copies_document of the SuppliersUpdateModel.

                - supplier_id (Union[str, int]): supplier_id of the SuppliersUpdateModel.

                - vat (str): vat of the SuppliersUpdateModel.

                - website (str): website of the SuppliersUpdateModel.

                - zip_code (str): zip_code of the SuppliersUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SuppliersUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
