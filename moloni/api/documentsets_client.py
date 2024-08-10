from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class DocumentsetsCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None


class DocumentsetsDeleteModel(BaseModel):
    company_id: Union[str, int]
    document_set_id: Optional[Union[str, int]] = None


class DocumentsetsGetAllModel(BaseModel):
    company_id: Union[str, int]


class DocumentsetsGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None


class DocumentsetsInsertModel(BaseModel):
    company_id: Union[str, int]
    active_by_default: Optional[str] = None
    cash_vat_scheme_indicator: Optional[str] = None
    name: Optional[str] = None
    template_id: Optional[Union[str, int]] = None


class DocumentsetsUpdateModel(BaseModel):
    company_id: Union[str, int]
    active_by_default: Optional[str] = None
    cash_vat_scheme_indicator: Optional[str] = None
    document_set_id: Optional[Union[str, int]] = None
    name: Optional[str] = None
    template_id: Optional[Union[str, int]] = None


class DocumentsetsClient(MoloniBaseClient):

    @endpoint("/<version>/documentSets/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[DocumentsetsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[DocumentsetsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[DocumentsetsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsetsCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the DocumentsetsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsetsCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documentSets/delete/", method="post")
    def delete(self, data: Union[DocumentsetsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[DocumentsetsDeleteModel, dict], **kwargs)

        Args:

            data (Union[DocumentsetsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsetsDeleteModel.

                - document_set_id (Union[str, int]): document_set_id of the DocumentsetsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsetsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documentSets/getAll/", method="post")
    def get_all(self, data: Union[DocumentsetsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[DocumentsetsGetAllModel, dict], **kwargs)

        Args:

            data (Union[DocumentsetsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsetsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsetsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documentSets/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[DocumentsetsGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[DocumentsetsGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[DocumentsetsGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsetsGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the DocumentsetsGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsetsGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documentSets/insert/", method="post")
    def insert(self, data: Union[DocumentsetsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[DocumentsetsInsertModel, dict], **kwargs)

        Args:

            data (Union[DocumentsetsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - active_by_default (str): active_by_default of the DocumentsetsInsertModel.

                - cash_vat_scheme_indicator (str): cash_vat_scheme_indicator of the DocumentsetsInsertModel.

                - company_id (Union[str, int]): company_id of the DocumentsetsInsertModel.

                - name (str): name of the DocumentsetsInsertModel.

                - template_id (Union[str, int]): template_id of the DocumentsetsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsetsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documentSets/update/", method="post")
    def update(self, data: Union[DocumentsetsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[DocumentsetsUpdateModel, dict], **kwargs)

        Args:

            data (Union[DocumentsetsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - active_by_default (str): active_by_default of the DocumentsetsUpdateModel.

                - cash_vat_scheme_indicator (str): cash_vat_scheme_indicator of the DocumentsetsUpdateModel.

                - company_id (Union[str, int]): company_id of the DocumentsetsUpdateModel.

                - document_set_id (Union[str, int]): document_set_id of the DocumentsetsUpdateModel.

                - name (str): name of the DocumentsetsUpdateModel.

                - template_id (Union[str, int]): template_id of the DocumentsetsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsetsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
