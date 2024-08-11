from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = TaxesClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class TaxesCountModifiedSinceModel(ApiRequestModel):
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


class TaxesDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    tax_id: Optional[Union[str, int]] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.delete(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class TaxesGetAllModel(ApiRequestModel):
    company_id: Union[str, int]

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_all(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class TaxesGetModifiedSinceModel(ApiRequestModel):
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


class TaxesInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    active_by_default: Optional[str] = None
    exemption_reason: Optional[str] = None
    fiscal_zone: Optional[str] = None
    name: Optional[str] = None
    saft_type: Optional[str] = None
    stamp_tax: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    vat_type: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.insert(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class TaxesUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    active_by_default: Optional[str] = None
    exemption_reason: Optional[str] = None
    fiscal_zone: Optional[str] = None
    name: Optional[str] = None
    saft_type: Optional[str] = None
    stamp_tax: Optional[str] = None
    tax_id: Optional[Union[str, int]] = None
    type: Optional[str] = None
    value: Optional[str] = None
    vat_type: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.update(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class TaxesClient(MoloniBaseClient):

    @endpoint("/<version>/taxes/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[TaxesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[TaxesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[TaxesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the TaxesCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the TaxesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, TaxesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/taxes/delete/", method="post")
    def delete(self, data: Union[TaxesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[TaxesDeleteModel, dict], **kwargs)

        Args:

            data (Union[TaxesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the TaxesDeleteModel.

                - tax_id (Union[str, int]): tax_id of the TaxesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, TaxesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/taxes/getAll/", method="post")
    def get_all(self, data: Union[TaxesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[TaxesGetAllModel, dict], **kwargs)

        Args:

            data (Union[TaxesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the TaxesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, TaxesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/taxes/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[TaxesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[TaxesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[TaxesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the TaxesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the TaxesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, TaxesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/taxes/insert/", method="post")
    def insert(self, data: Union[TaxesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[TaxesInsertModel, dict], **kwargs)

        Args:

            data (Union[TaxesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - active_by_default (str): active_by_default of the TaxesInsertModel.

                - company_id (Union[str, int]): company_id of the TaxesInsertModel.

                - exemption_reason (str): exemption_reason of the TaxesInsertModel.

                - fiscal_zone (str): fiscal_zone of the TaxesInsertModel.

                - name (str): name of the TaxesInsertModel.

                - saft_type (str): saft_type of the TaxesInsertModel.

                - stamp_tax (str): stamp_tax of the TaxesInsertModel.

                - type (str): type of the TaxesInsertModel.

                - value (str): value of the TaxesInsertModel.

                - vat_type (str): vat_type of the TaxesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, TaxesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/taxes/update/", method="post")
    def update(self, data: Union[TaxesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[TaxesUpdateModel, dict], **kwargs)

        Args:

            data (Union[TaxesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - active_by_default (str): active_by_default of the TaxesUpdateModel.

                - company_id (Union[str, int]): company_id of the TaxesUpdateModel.

                - exemption_reason (str): exemption_reason of the TaxesUpdateModel.

                - fiscal_zone (str): fiscal_zone of the TaxesUpdateModel.

                - name (str): name of the TaxesUpdateModel.

                - saft_type (str): saft_type of the TaxesUpdateModel.

                - stamp_tax (str): stamp_tax of the TaxesUpdateModel.

                - tax_id (Union[str, int]): tax_id of the TaxesUpdateModel.

                - type (str): type of the TaxesUpdateModel.

                - value (str): value of the TaxesUpdateModel.

                - vat_type (str): vat_type of the TaxesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, TaxesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
