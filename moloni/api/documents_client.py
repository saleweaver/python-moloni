from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class DocumentsCountModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    our_reference: str
    salesman_id: Union[str, int]
    supplier_id: Union[str, int]
    year: str
    your_reference: str


class DocumentsGetAllModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    offset: Union[str, int] = 0
    our_reference: str
    qty: Union[str, int] = 25
    salesman_id: Union[str, int]
    supplier_id: Union[str, int]
    year: str
    your_reference: str


class DocumentsGetAllDocumentTypesModel(BaseModel):
    language_id: Union[str, int]


class DocumentsGetOneModel(BaseModel):
    company_id: Union[str, int]
    customer_id: Union[str, int]
    date: str
    document_id: Union[str, int]
    document_set_id: Union[str, int]
    expiration_date: str
    number: str
    our_reference: str
    salesman_id: Union[str, int]
    supplier_id: Union[str, int]
    year: str
    your_reference: str


class DocumentsGetPdfLinkModel(BaseModel):
    company_id: Union[str, int]
    document_id: Union[str, int]


class DocumentsClient(MoloniBaseClient):

    @endpoint("/<version>/documents/count/", method="post")
    def count(self, data: Union[DocumentsCountModel, dict], **kwargs):
        """
        count(self, data: Union[DocumentsCountModel, dict], **kwargs)

        Args:

            data (Union[DocumentsCountModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsCountModel.

                - customer_id (Union[str, int]): customer_id of the DocumentsCountModel.

                - date (str): date of the DocumentsCountModel.

                - document_set_id (Union[str, int]): document_set_id of the DocumentsCountModel.

                - expiration_date (str): expiration_date of the DocumentsCountModel.

                - number (str): number of the DocumentsCountModel.

                - our_reference (str): our_reference of the DocumentsCountModel.

                - salesman_id (Union[str, int]): salesman_id of the DocumentsCountModel.

                - supplier_id (Union[str, int]): supplier_id of the DocumentsCountModel.

                - year (str): year of the DocumentsCountModel.

                - your_reference (str): your_reference of the DocumentsCountModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsCountModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documents/getAll/", method="post")
    def get_all(self, data: Union[DocumentsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[DocumentsGetAllModel, dict], **kwargs)

        Args:

            data (Union[DocumentsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsGetAllModel.

                - customer_id (Union[str, int]): customer_id of the DocumentsGetAllModel.

                - date (str): date of the DocumentsGetAllModel.

                - document_set_id (Union[str, int]): document_set_id of the DocumentsGetAllModel.

                - expiration_date (str): expiration_date of the DocumentsGetAllModel.

                - number (str): number of the DocumentsGetAllModel.

                - offset (str): offset of the DocumentsGetAllModel.

                - our_reference (str): our_reference of the DocumentsGetAllModel.

                - qty (str): qty of the DocumentsGetAllModel.

                - salesman_id (Union[str, int]): salesman_id of the DocumentsGetAllModel.

                - supplier_id (Union[str, int]): supplier_id of the DocumentsGetAllModel.

                - year (str): year of the DocumentsGetAllModel.

                - your_reference (str): your_reference of the DocumentsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documents/getAllDocumentTypes/", method="post")
    def get_all_document_types(
        self, data: Union[DocumentsGetAllDocumentTypesModel, dict], **kwargs
    ):
        """
        get_all_document_types(self, data: Union[DocumentsGetAllDocumentTypesModel, dict], **kwargs)

        Args:

            data (Union[DocumentsGetAllDocumentTypesModel, dict]): A model instance or dictionary containing the following fields:

                - language_id (Union[str, int]): language_id of the DocumentsGetAllDocumentTypesModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsGetAllDocumentTypesModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documents/getOne/", method="post")
    def get_one(self, data: Union[DocumentsGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[DocumentsGetOneModel, dict], **kwargs)

        Args:

            data (Union[DocumentsGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsGetOneModel.

                - customer_id (Union[str, int]): customer_id of the DocumentsGetOneModel.

                - date (str): date of the DocumentsGetOneModel.

                - document_id (Union[str, int]): document_id of the DocumentsGetOneModel.

                - document_set_id (Union[str, int]): document_set_id of the DocumentsGetOneModel.

                - expiration_date (str): expiration_date of the DocumentsGetOneModel.

                - number (str): number of the DocumentsGetOneModel.

                - our_reference (str): our_reference of the DocumentsGetOneModel.

                - salesman_id (Union[str, int]): salesman_id of the DocumentsGetOneModel.

                - supplier_id (Union[str, int]): supplier_id of the DocumentsGetOneModel.

                - year (str): year of the DocumentsGetOneModel.

                - your_reference (str): your_reference of the DocumentsGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/documents/getPDFLink/", method="post")
    def get_pdf_link(self, data: Union[DocumentsGetPdfLinkModel, dict], **kwargs):
        """
        get_pdf_link(self, data: Union[DocumentsGetPdfLinkModel, dict], **kwargs)

        Args:

            data (Union[DocumentsGetPdfLinkModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the DocumentsGetPdfLinkModel.

                - document_id (Union[str, int]): document_id of the DocumentsGetPdfLinkModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, DocumentsGetPdfLinkModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
