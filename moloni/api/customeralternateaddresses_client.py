from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = CustomeralternateaddressesClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class CustomeralternateaddressesCountModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.count_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class CustomeralternateaddressesDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    address_id: Optional[Union[str, int]] = None
    customer_id: Optional[Union[str, int]] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.delete(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class CustomeralternateaddressesGetAllModel(ApiRequestModel):
    company_id: Union[str, int]
    customer_id: Optional[Union[str, int]] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_all(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class CustomeralternateaddressesGetModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None
    offset: Optional[Union[str, int]] = 0
    qty: Optional[Union[str, int]] = 25

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class CustomeralternateaddressesInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    city: Optional[str] = None
    code: Optional[str] = None
    contact_name: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    customer_id: Optional[Union[str, int]] = None
    designation: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    phone: Optional[str] = None
    zip_code: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.insert(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class CustomeralternateaddressesUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    address_id: Optional[Union[str, int]] = None
    city: Optional[str] = None
    code: Optional[str] = None
    contact_name: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    customer_id: Optional[Union[str, int]] = None
    designation: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    phone: Optional[str] = None
    zip_code: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.update(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class CustomeralternateaddressesClient(MoloniBaseClient):

    @endpoint(
        "/<version>/customerAlternateAddresses/countModifiedSince/", method="post"
    )
    def count_modified_since(
        self,
        data: Union[CustomeralternateaddressesCountModifiedSinceModel, dict],
        **kwargs
    ):
        """
        count_modified_since(self, data: Union[CustomeralternateaddressesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[CustomeralternateaddressesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomeralternateaddressesCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the CustomeralternateaddressesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, CustomeralternateaddressesCountModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerAlternateAddresses/delete/", method="post")
    def delete(
        self, data: Union[CustomeralternateaddressesDeleteModel, dict], **kwargs
    ):
        """
        delete(self, data: Union[CustomeralternateaddressesDeleteModel, dict], **kwargs)

        Args:

            data (Union[CustomeralternateaddressesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - address_id (Union[str, int]): address_id of the CustomeralternateaddressesDeleteModel.

                - company_id (Union[str, int]): company_id of the CustomeralternateaddressesDeleteModel.

                - customer_id (Union[str, int]): customer_id of the CustomeralternateaddressesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomeralternateaddressesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerAlternateAddresses/getAll/", method="post")
    def get_all(
        self, data: Union[CustomeralternateaddressesGetAllModel, dict], **kwargs
    ):
        """
        get_all(self, data: Union[CustomeralternateaddressesGetAllModel, dict], **kwargs)

        Args:

            data (Union[CustomeralternateaddressesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomeralternateaddressesGetAllModel.

                - customer_id (Union[str, int]): customer_id of the CustomeralternateaddressesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomeralternateaddressesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerAlternateAddresses/getModifiedSince/", method="post")
    def get_modified_since(
        self,
        data: Union[CustomeralternateaddressesGetModifiedSinceModel, dict],
        **kwargs
    ):
        """
        get_modified_since(self, data: Union[CustomeralternateaddressesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[CustomeralternateaddressesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CustomeralternateaddressesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the CustomeralternateaddressesGetModifiedSinceModel.

                - offset (str): offset of the CustomeralternateaddressesGetModifiedSinceModel.

                - qty (str): qty of the CustomeralternateaddressesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, CustomeralternateaddressesGetModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerAlternateAddresses/insert/", method="post")
    def insert(
        self, data: Union[CustomeralternateaddressesInsertModel, dict], **kwargs
    ):
        """
        insert(self, data: Union[CustomeralternateaddressesInsertModel, dict], **kwargs)

        Args:

            data (Union[CustomeralternateaddressesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the CustomeralternateaddressesInsertModel.

                - city (str): city of the CustomeralternateaddressesInsertModel.

                - code (str): code of the CustomeralternateaddressesInsertModel.

                - company_id (Union[str, int]): company_id of the CustomeralternateaddressesInsertModel.

                - contact_name (str): contact_name of the CustomeralternateaddressesInsertModel.

                - country_id (Union[str, int]): country_id of the CustomeralternateaddressesInsertModel.

                - customer_id (Union[str, int]): customer_id of the CustomeralternateaddressesInsertModel.

                - designation (str): designation of the CustomeralternateaddressesInsertModel.

                - email (str): email of the CustomeralternateaddressesInsertModel.

                - fax (str): fax of the CustomeralternateaddressesInsertModel.

                - phone (str): phone of the CustomeralternateaddressesInsertModel.

                - zip_code (str): zip_code of the CustomeralternateaddressesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomeralternateaddressesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/customerAlternateAddresses/update/", method="post")
    def update(
        self, data: Union[CustomeralternateaddressesUpdateModel, dict], **kwargs
    ):
        """
        update(self, data: Union[CustomeralternateaddressesUpdateModel, dict], **kwargs)

        Args:

            data (Union[CustomeralternateaddressesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the CustomeralternateaddressesUpdateModel.

                - address_id (Union[str, int]): address_id of the CustomeralternateaddressesUpdateModel.

                - city (str): city of the CustomeralternateaddressesUpdateModel.

                - code (str): code of the CustomeralternateaddressesUpdateModel.

                - company_id (Union[str, int]): company_id of the CustomeralternateaddressesUpdateModel.

                - contact_name (str): contact_name of the CustomeralternateaddressesUpdateModel.

                - country_id (Union[str, int]): country_id of the CustomeralternateaddressesUpdateModel.

                - customer_id (Union[str, int]): customer_id of the CustomeralternateaddressesUpdateModel.

                - designation (str): designation of the CustomeralternateaddressesUpdateModel.

                - email (str): email of the CustomeralternateaddressesUpdateModel.

                - fax (str): fax of the CustomeralternateaddressesUpdateModel.

                - phone (str): phone of the CustomeralternateaddressesUpdateModel.

                - zip_code (str): zip_code of the CustomeralternateaddressesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CustomeralternateaddressesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
