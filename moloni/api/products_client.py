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


class ProductsCountModel(BaseModel):
    company_id: Union[str, int]
    category_id: Optional[Union[str, int]] = None


class ProductsCountByEanModel(BaseModel):
    company_id: Union[str, int]
    ean: Optional[str] = None


class ProductsCountByNameModel(BaseModel):
    company_id: Union[str, int]
    name: Optional[str] = None


class ProductsCountByReferenceModel(BaseModel):
    company_id: Union[str, int]
    reference: Optional[str] = None


class ProductsCountBySearchModel(BaseModel):
    company_id: Union[str, int]
    search: Optional[str] = None


class ProductsCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None


class ProductsDeleteModel(BaseModel):
    company_id: Union[str, int]
    product_id: Optional[Union[str, int]] = None


class ProductsGetAllModel(BaseModel):
    company_id: Union[str, int]
    category_id: Optional[Union[str, int]] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25


class ProductsGetByEanModel(BaseModel):
    company_id: Union[str, int]
    ean: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25


class ProductsGetByNameModel(BaseModel):
    company_id: Union[str, int]
    name: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25


class ProductsGetByReferenceModel(BaseModel):
    company_id: Union[str, int]
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25
    reference: Optional[str] = None


class ProductsGetBySearchModel(BaseModel):
    company_id: Union[str, int]
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25
    search: Optional[str] = None


class ProductsGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25


class ProductsGetOneModel(BaseModel):
    company_id: Union[str, int]
    product_id: Optional[Union[str, int]] = None


class ProductsInsertModel(BaseModel):
    company_id: Union[str, int]
    at_product_category: Optional[str] = None
    category_id: Optional[Union[str, int]] = None
    ean: Optional[str] = None
    exemption_reason: Optional[str] = None
    has_stock: Optional[str] = None
    name: Optional[str] = None
    pos_favorite: Optional[str] = None
    price: Optional[str] = None
    reference: Optional[str] = None
    stock: Optional[str] = None
    summary: Optional[str] = None
    suppliers: Optional[List[Suppliers]] = None
    taxes: Optional[List[Taxes]] = None
    type: Optional[str] = None
    unit_id: Optional[Union[str, int]] = None
    warehouse_id: Optional[Union[str, int]] = None
    warehouses: Optional[List[Warehouses]] = None


class ProductsUpdateModel(BaseModel):
    company_id: Union[str, int]
    at_product_category: Optional[str] = None
    category_id: Optional[Union[str, int]] = None
    ean: Optional[str] = None
    exemption_reason: Optional[str] = None
    has_stock: Optional[str] = None
    name: Optional[str] = None
    pos_favorite: Optional[str] = None
    price: Optional[str] = None
    product_id: Optional[Union[str, int]] = None
    reference: Optional[str] = None
    stock: Optional[str] = None
    summary: Optional[str] = None
    suppliers: Optional[List[Suppliers]] = None
    taxes: Optional[List[Taxes]] = None
    type: Optional[str] = None
    unit_id: Optional[Union[str, int]] = None
    warehouse_id: Optional[Union[str, int]] = None


class ProductsClient(MoloniBaseClient):

    @endpoint("/<version>/products/count/", method="post")
    def count(self, data: Union[ProductsCountModel, dict], **kwargs):
        """
        count(self, data: Union[ProductsCountModel, dict], **kwargs)

        Args:

            data (Union[ProductsCountModel, dict]): A model instance or dictionary containing the following fields:

                - category_id (Union[str, int]): category_id of the ProductsCountModel.

                - company_id (Union[str, int]): company_id of the ProductsCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/countByEAN/", method="post")
    def count_by_ean(self, data: Union[ProductsCountByEanModel, dict], **kwargs):
        """
        count_by_ean(self, data: Union[ProductsCountByEanModel, dict], **kwargs)

        Args:

            data (Union[ProductsCountByEanModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsCountByEanModel.

                - ean (str): ean of the ProductsCountByEanModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsCountByEanModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/countByName/", method="post")
    def count_by_name(self, data: Union[ProductsCountByNameModel, dict], **kwargs):
        """
        count_by_name(self, data: Union[ProductsCountByNameModel, dict], **kwargs)

        Args:

            data (Union[ProductsCountByNameModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsCountByNameModel.

                - name (str): name of the ProductsCountByNameModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsCountByNameModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/countByReference/", method="post")
    def count_by_reference(
        self, data: Union[ProductsCountByReferenceModel, dict], **kwargs
    ):
        """
        count_by_reference(self, data: Union[ProductsCountByReferenceModel, dict], **kwargs)

        Args:

            data (Union[ProductsCountByReferenceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsCountByReferenceModel.

                - reference (str): reference of the ProductsCountByReferenceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsCountByReferenceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/countBySearch/", method="post")
    def count_by_search(self, data: Union[ProductsCountBySearchModel, dict], **kwargs):
        """
        count_by_search(self, data: Union[ProductsCountBySearchModel, dict], **kwargs)

        Args:

            data (Union[ProductsCountBySearchModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsCountBySearchModel.

                - search (str): search of the ProductsCountBySearchModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsCountBySearchModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[ProductsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[ProductsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[ProductsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the ProductsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/delete/", method="post")
    def delete(self, data: Union[ProductsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[ProductsDeleteModel, dict], **kwargs)

        Args:

            data (Union[ProductsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsDeleteModel.

                - product_id (Union[str, int]): product_id of the ProductsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/getAll/", method="post")
    def get_all(self, data: Union[ProductsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[ProductsGetAllModel, dict], **kwargs)

        Args:

            data (Union[ProductsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - category_id (Union[str, int]): category_id of the ProductsGetAllModel.

                - company_id (Union[str, int]): company_id of the ProductsGetAllModel.

                - offset (str): offset of the ProductsGetAllModel.

                - qty (str): qty of the ProductsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/getByEAN/", method="post")
    def get_by_ean(self, data: Union[ProductsGetByEanModel, dict], **kwargs):
        """
        get_by_ean(self, data: Union[ProductsGetByEanModel, dict], **kwargs)

        Args:

            data (Union[ProductsGetByEanModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsGetByEanModel.

                - ean (str): ean of the ProductsGetByEanModel.

                - offset (str): offset of the ProductsGetByEanModel.

                - qty (str): qty of the ProductsGetByEanModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsGetByEanModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/getByName/", method="post")
    def get_by_name(self, data: Union[ProductsGetByNameModel, dict], **kwargs):
        """
        get_by_name(self, data: Union[ProductsGetByNameModel, dict], **kwargs)

        Args:

            data (Union[ProductsGetByNameModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsGetByNameModel.

                - name (str): name of the ProductsGetByNameModel.

                - offset (str): offset of the ProductsGetByNameModel.

                - qty (str): qty of the ProductsGetByNameModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsGetByNameModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/getByReference/", method="post")
    def get_by_reference(
        self, data: Union[ProductsGetByReferenceModel, dict], **kwargs
    ):
        """
        get_by_reference(self, data: Union[ProductsGetByReferenceModel, dict], **kwargs)

        Args:

            data (Union[ProductsGetByReferenceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsGetByReferenceModel.

                - offset (str): offset of the ProductsGetByReferenceModel.

                - qty (str): qty of the ProductsGetByReferenceModel.

                - reference (str): reference of the ProductsGetByReferenceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsGetByReferenceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/getBySearch/", method="post")
    def get_by_search(self, data: Union[ProductsGetBySearchModel, dict], **kwargs):
        """
        get_by_search(self, data: Union[ProductsGetBySearchModel, dict], **kwargs)

        Args:

            data (Union[ProductsGetBySearchModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsGetBySearchModel.

                - offset (str): offset of the ProductsGetBySearchModel.

                - qty (str): qty of the ProductsGetBySearchModel.

                - search (str): search of the ProductsGetBySearchModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsGetBySearchModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[ProductsGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[ProductsGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[ProductsGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the ProductsGetModifiedSinceModel.

                - offset (str): offset of the ProductsGetModifiedSinceModel.

                - qty (str): qty of the ProductsGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/getOne/", method="post")
    def get_one(self, data: Union[ProductsGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[ProductsGetOneModel, dict], **kwargs)

        Args:

            data (Union[ProductsGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the ProductsGetOneModel.

                - product_id (Union[str, int]): product_id of the ProductsGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/insert/", method="post")
    def insert(self, data: Union[ProductsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[ProductsInsertModel, dict], **kwargs)

        Args:

            data (Union[ProductsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - at_product_category (str): at_product_category of the ProductsInsertModel.

                - category_id (Union[str, int]): category_id of the ProductsInsertModel.

                - company_id (Union[str, int]): company_id of the ProductsInsertModel.

                - ean (str): ean of the ProductsInsertModel.

                - exemption_reason (str): exemption_reason of the ProductsInsertModel.

                - has_stock (str): has_stock of the ProductsInsertModel.

                - name (str): name of the ProductsInsertModel.

                - pos_favorite (str): pos_favorite of the ProductsInsertModel.

                - price (str): price of the ProductsInsertModel.

                - reference (str): reference of the ProductsInsertModel.

                - stock (str): stock of the ProductsInsertModel.

                - summary (str): summary of the ProductsInsertModel.

                - suppliers (str): suppliers of the ProductsInsertModel.

                - taxes (str): taxes of the ProductsInsertModel.

                - type (str): type of the ProductsInsertModel.

                - unit_id (Union[str, int]): unit_id of the ProductsInsertModel.

                - warehouse_id (Union[str, int]): warehouse_id of the ProductsInsertModel.

                - warehouses (str): warehouses of the ProductsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/products/update/", method="post")
    def update(self, data: Union[ProductsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[ProductsUpdateModel, dict], **kwargs)

        Args:

            data (Union[ProductsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - at_product_category (str): at_product_category of the ProductsUpdateModel.

                - category_id (Union[str, int]): category_id of the ProductsUpdateModel.

                - company_id (Union[str, int]): company_id of the ProductsUpdateModel.

                - ean (str): ean of the ProductsUpdateModel.

                - exemption_reason (str): exemption_reason of the ProductsUpdateModel.

                - has_stock (str): has_stock of the ProductsUpdateModel.

                - name (str): name of the ProductsUpdateModel.

                - pos_favorite (str): pos_favorite of the ProductsUpdateModel.

                - price (str): price of the ProductsUpdateModel.

                - product_id (Union[str, int]): product_id of the ProductsUpdateModel.

                - reference (str): reference of the ProductsUpdateModel.

                - stock (str): stock of the ProductsUpdateModel.

                - summary (str): summary of the ProductsUpdateModel.

                - suppliers (str): suppliers of the ProductsUpdateModel.

                - taxes (str): taxes of the ProductsUpdateModel.

                - type (str): type of the ProductsUpdateModel.

                - unit_id (Union[str, int]): unit_id of the ProductsUpdateModel.

                - warehouse_id (Union[str, int]): warehouse_id of the ProductsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, ProductsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
