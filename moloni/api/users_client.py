from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = UsersClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class Suppliers(BaseModel):
    cost_price: Optional[Any] = None
    supplier_id: Optional[Any] = None


class Taxes(BaseModel):
    cumulative: Optional[Any] = None
    order: Optional[Any] = None
    tax_id: Optional[Any] = None
    value: Optional[Any] = None


class Warehouses(BaseModel):
    stock: Optional[Any] = None
    warehouse_id: Optional[Any] = None


class UsersGetAllModel(ApiRequestModel):
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


class UsersClient(MoloniBaseClient):

    @endpoint("/<version>/users/getAll/", method="post")
    def get_all(self, data: Union[UsersGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[UsersGetAllModel, dict], **kwargs)

        Args:

            data (Union[UsersGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the UsersGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, UsersGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
