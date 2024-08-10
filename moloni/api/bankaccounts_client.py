from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class BankaccountsCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class BankaccountsDeleteModel(BaseModel):
    bank_account_id: Union[str, int]
    company_id: Union[str, int]


class BankaccountsGetAllModel(BaseModel):
    company_id: Union[str, int]


class BankaccountsInsertModel(BaseModel):
    company_id: Union[str, int]
    name: str
    order: str
    value: str


class BankaccountsUpdateModel(BaseModel):
    bank_account_id: Union[str, int]
    company_id: Union[str, int]
    name: str = None
    order: str = None
    value: str = None


class BankaccountsClient(MoloniBaseClient):

    @endpoint("/<version>/bankAccounts/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[BankaccountsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[BankaccountsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[BankaccountsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the BankaccountsCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the BankaccountsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BankaccountsCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/bankAccounts/delete/", method="post")
    def delete(self, data: Union[BankaccountsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[BankaccountsDeleteModel, dict], **kwargs)

        Args:

            data (Union[BankaccountsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - bank_account_id (Union[str, int]): bank_account_id of the BankaccountsDeleteModel.

                - company_id (Union[str, int]): company_id of the BankaccountsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BankaccountsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/bankAccounts/getAll/", method="post")
    def get_all(self, data: Union[BankaccountsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[BankaccountsGetAllModel, dict], **kwargs)

        Args:

            data (Union[BankaccountsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the BankaccountsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BankaccountsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/bankAccounts/insert/", method="post")
    def insert(self, data: Union[BankaccountsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[BankaccountsInsertModel, dict], **kwargs)

        Args:

            data (Union[BankaccountsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the BankaccountsInsertModel.

                - name (str): name of the BankaccountsInsertModel.

                - order (str): order of the BankaccountsInsertModel.

                - value (str): value of the BankaccountsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BankaccountsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/bankAccounts/update/", method="post")
    def update(self, data: Union[BankaccountsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[BankaccountsUpdateModel, dict], **kwargs)

        Args:

            data (Union[BankaccountsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - bank_account_id (Union[str, int]): bank_account_id of the BankaccountsUpdateModel.

                - company_id (Union[str, int]): company_id of the BankaccountsUpdateModel.

                - name (str): name of the BankaccountsUpdateModel.

                - order (str): order of the BankaccountsUpdateModel.

                - value (str): value of the BankaccountsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, BankaccountsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
