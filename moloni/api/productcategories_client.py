from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ProductcategoriesDeleteModel(BaseModel):
    category_id: Union[str, int]
    company_id: Union[str, int]


class ProductcategoriesGetAllModel(BaseModel):
    company_id: Union[str, int]
    parent_id: Union[str, int]


class ProductcategoriesGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class ProductcategoriesInsertModel(BaseModel):
    company_id: Union[str, int]
    description: str
    name: str
    parent_id: Union[str, int]
    pos_enabled: str


class ProductcategoriesUpdateModel(BaseModel):
    category_id: Union[str, int]
    company_id: Union[str, int]
    description: str = None
    name: str = None
    parent_id: Union[str, int] = None
    pos_enabled: str = None


class ProductcategoriesClient(MoloniBaseClient):

    @endpoint("/<version>/productCategories/delete/", method="post")
    def delete(self, data: Union[ProductcategoriesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[ProductcategoriesDeleteModel, dict], **kwargs)

        Args:

            data (Union[ProductcategoriesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - category_id (Union[str, int]): category_id of the ProductcategoriesDeleteModel.

                - company_id (Union[str, int]): company_id of the ProductcategoriesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductcategoriesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/productCategories/getAll/", method="post")
    def get_all(self, data: Union[ProductcategoriesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[ProductcategoriesGetAllModel, dict], **kwargs)

        Args:

            data (Union[ProductcategoriesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductcategoriesGetAllModel.

                - parent_id (Union[str, int]): parent_id of the ProductcategoriesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductcategoriesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/productCategories/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[ProductcategoriesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[ProductcategoriesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[ProductcategoriesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductcategoriesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the ProductcategoriesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, ProductcategoriesGetModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/productCategories/insert/", method="post")
    def insert(self, data: Union[ProductcategoriesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[ProductcategoriesInsertModel, dict], **kwargs)

        Args:

            data (Union[ProductcategoriesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductcategoriesInsertModel.

                - description (str): description of the ProductcategoriesInsertModel.

                - name (str): name of the ProductcategoriesInsertModel.

                - parent_id (Union[str, int]): parent_id of the ProductcategoriesInsertModel.

                - pos_enabled (str): pos_enabled of the ProductcategoriesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductcategoriesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/productCategories/update/", method="post")
    def update(self, data: Union[ProductcategoriesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[ProductcategoriesUpdateModel, dict], **kwargs)

        Args:

            data (Union[ProductcategoriesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - category_id (Union[str, int]): category_id of the ProductcategoriesUpdateModel.

                - company_id (Union[str, int]): company_id of the ProductcategoriesUpdateModel.

                - description (str): description of the ProductcategoriesUpdateModel.

                - name (str): name of the ProductcategoriesUpdateModel.

                - parent_id (Union[str, int]): parent_id of the ProductcategoriesUpdateModel.

                - pos_enabled (str): pos_enabled of the ProductcategoriesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductcategoriesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
