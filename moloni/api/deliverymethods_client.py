from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class DeliverymethodsCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class DeliverymethodsDeleteModel(BaseModel):
    company_id: Union[str, int]
    delivery_method_id: Union[str, int]


class DeliverymethodsGetAllModel(BaseModel):
    company_id: Union[str, int]


class DeliverymethodsGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class DeliverymethodsInsertModel(BaseModel):
    company_id: Union[str, int]
    name: str


class DeliverymethodsUpdateModel(BaseModel):
    company_id: Union[str, int]
    delivery_method_id: Union[str, int]
    name: str = None


class DeliverymethodsClient(MoloniBaseClient):

    @endpoint("/<version>/deliveryMethods/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[DeliverymethodsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[DeliverymethodsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[DeliverymethodsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverymethodsCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the DeliverymethodsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, DeliverymethodsCountModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryMethods/delete/", method="post")
    def delete(self, data: Union[DeliverymethodsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[DeliverymethodsDeleteModel, dict], **kwargs)

        Args:

            data (Union[DeliverymethodsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverymethodsDeleteModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the DeliverymethodsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverymethodsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryMethods/getAll/", method="post")
    def get_all(self, data: Union[DeliverymethodsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[DeliverymethodsGetAllModel, dict], **kwargs)

        Args:

            data (Union[DeliverymethodsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverymethodsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverymethodsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryMethods/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[DeliverymethodsGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[DeliverymethodsGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[DeliverymethodsGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverymethodsGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the DeliverymethodsGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverymethodsGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryMethods/insert/", method="post")
    def insert(self, data: Union[DeliverymethodsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[DeliverymethodsInsertModel, dict], **kwargs)

        Args:

            data (Union[DeliverymethodsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverymethodsInsertModel.

                - name (str): name of the DeliverymethodsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverymethodsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/deliveryMethods/update/", method="post")
    def update(self, data: Union[DeliverymethodsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[DeliverymethodsUpdateModel, dict], **kwargs)

        Args:

            data (Union[DeliverymethodsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DeliverymethodsUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the DeliverymethodsUpdateModel.

                - name (str): name of the DeliverymethodsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DeliverymethodsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
