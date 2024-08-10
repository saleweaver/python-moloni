from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class Suppliers(BaseModel):
    cost_price: Optional[Union[str, int]]
    supplier_id: Optional[Union[str, int]]


class Taxes(BaseModel):
    cumulative: Optional[Union[str, int]]
    order: Optional[Union[str, int]]
    tax_id: Optional[Union[str, int]]
    value: Optional[Union[str, int]]


class Warehouses(BaseModel):
    stock: Optional[Union[str, int]]
    warehouse_id: Optional[Union[str, int]]


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
