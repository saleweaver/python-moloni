from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class Suppliers(BaseModel):
    cost_price: str
    supplier_id: str


class Taxes(BaseModel):
    cumulative: str
    order: str
    tax_id: str
    value: str


class Warehouses(BaseModel):
    stock: str
    warehouse_id: str


class UsersGetAllModel(BaseModel):
    company_id: Union[str, int]


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
