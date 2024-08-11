from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = PaymentmethodsClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class PaymentmethodsCountModifiedSinceModel(ApiRequestModel):
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


class PaymentmethodsDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    payment_method_id: Optional[Union[str, int]] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.delete(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class PaymentmethodsGetAllModel(ApiRequestModel):
    company_id: Union[str, int]

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_all(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class PaymentmethodsGetModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class PaymentmethodsInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    name: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.insert(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class PaymentmethodsUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    name: Optional[str] = None
    payment_method_id: Optional[Union[str, int]] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.update(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class PaymentmethodsClient(MoloniBaseClient):

    @endpoint("/<version>/paymentMethods/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[PaymentmethodsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[PaymentmethodsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[PaymentmethodsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the PaymentmethodsCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the PaymentmethodsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, PaymentmethodsCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/paymentMethods/delete/", method="post")
    def delete(self, data: Union[PaymentmethodsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[PaymentmethodsDeleteModel, dict], **kwargs)

        Args:

            data (Union[PaymentmethodsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the PaymentmethodsDeleteModel.

                - payment_method_id (Union[str, int]): payment_method_id of the PaymentmethodsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, PaymentmethodsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/paymentMethods/getAll/", method="post")
    def get_all(self, data: Union[PaymentmethodsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[PaymentmethodsGetAllModel, dict], **kwargs)

        Args:

            data (Union[PaymentmethodsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the PaymentmethodsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, PaymentmethodsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/paymentMethods/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[PaymentmethodsGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[PaymentmethodsGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[PaymentmethodsGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the PaymentmethodsGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the PaymentmethodsGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, PaymentmethodsGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/paymentMethods/insert/", method="post")
    def insert(self, data: Union[PaymentmethodsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[PaymentmethodsInsertModel, dict], **kwargs)

        Args:

            data (Union[PaymentmethodsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the PaymentmethodsInsertModel.

                - name (str): name of the PaymentmethodsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, PaymentmethodsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/paymentMethods/update/", method="post")
    def update(self, data: Union[PaymentmethodsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[PaymentmethodsUpdateModel, dict], **kwargs)

        Args:

            data (Union[PaymentmethodsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the PaymentmethodsUpdateModel.

                - name (str): name of the PaymentmethodsUpdateModel.

                - payment_method_id (Union[str, int]): payment_method_id of the PaymentmethodsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, PaymentmethodsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
