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


class SubscriptionGetOneModel(BaseModel):
    company_id: Union[str, int]


class SubscriptionClient(MoloniBaseClient):

    @endpoint("/<version>/subscription/getOne/", method="post")
    def get_one(self, data: Union[SubscriptionGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[SubscriptionGetOneModel, dict], **kwargs)

        Args:

            data (Union[SubscriptionGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the SubscriptionGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, SubscriptionGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
