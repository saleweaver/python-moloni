from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class IdentificationtemplatesCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None


class IdentificationtemplatesDeleteModel(BaseModel):
    company_id: Union[str, int]
    template_id: Optional[Union[str, int]] = None


class IdentificationtemplatesGetAllModel(BaseModel):
    company_id: Union[str, int]


class IdentificationtemplatesGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None


class IdentificationtemplatesInsertModel(BaseModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    business_name: Optional[str] = None
    city: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    documents_footnote: Optional[str] = None
    email: Optional[str] = None
    email_sender_address: Optional[str] = None
    email_sender_name: Optional[str] = None
    fax: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    zip_code: Optional[str] = None


class IdentificationtemplatesUpdateModel(BaseModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    business_name: Optional[str] = None
    city: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    documents_footnote: Optional[str] = None
    email: Optional[str] = None
    email_sender_address: Optional[str] = None
    email_sender_name: Optional[str] = None
    fax: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    phone: Optional[str] = None
    template_id: Optional[Union[str, int]] = None
    website: Optional[str] = None
    zip_code: Optional[str] = None


class IdentificationtemplatesClient(MoloniBaseClient):

    @endpoint("/<version>/identificationTemplates/countModifiedSince/", method="post")
    def count_modified_since(
        self,
        data: Union[IdentificationtemplatesCountModifiedSinceModel, dict],
        **kwargs
    ):
        """
        count_modified_since(self, data: Union[IdentificationtemplatesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the IdentificationtemplatesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, IdentificationtemplatesCountModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/delete/", method="post")
    def delete(self, data: Union[IdentificationtemplatesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[IdentificationtemplatesDeleteModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesDeleteModel.

                - template_id (Union[str, int]): template_id of the IdentificationtemplatesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, IdentificationtemplatesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/getAll/", method="post")
    def get_all(self, data: Union[IdentificationtemplatesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[IdentificationtemplatesGetAllModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, IdentificationtemplatesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[IdentificationtemplatesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[IdentificationtemplatesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the IdentificationtemplatesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, IdentificationtemplatesGetModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/insert/", method="post")
    def insert(self, data: Union[IdentificationtemplatesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[IdentificationtemplatesInsertModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the IdentificationtemplatesInsertModel.

                - business_name (str): business_name of the IdentificationtemplatesInsertModel.

                - city (str): city of the IdentificationtemplatesInsertModel.

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesInsertModel.

                - country_id (Union[str, int]): country_id of the IdentificationtemplatesInsertModel.

                - documents_footnote (str): documents_footnote of the IdentificationtemplatesInsertModel.

                - email (str): email of the IdentificationtemplatesInsertModel.

                - email_sender_address (str): email_sender_address of the IdentificationtemplatesInsertModel.

                - email_sender_name (str): email_sender_name of the IdentificationtemplatesInsertModel.

                - fax (str): fax of the IdentificationtemplatesInsertModel.

                - name (str): name of the IdentificationtemplatesInsertModel.

                - notes (str): notes of the IdentificationtemplatesInsertModel.

                - phone (str): phone of the IdentificationtemplatesInsertModel.

                - website (str): website of the IdentificationtemplatesInsertModel.

                - zip_code (str): zip_code of the IdentificationtemplatesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, IdentificationtemplatesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/identificationTemplates/update/", method="post")
    def update(self, data: Union[IdentificationtemplatesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[IdentificationtemplatesUpdateModel, dict], **kwargs)

        Args:

            data (Union[IdentificationtemplatesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the IdentificationtemplatesUpdateModel.

                - business_name (str): business_name of the IdentificationtemplatesUpdateModel.

                - city (str): city of the IdentificationtemplatesUpdateModel.

                - company_id (Union[str, int]): company_id of the IdentificationtemplatesUpdateModel.

                - country_id (Union[str, int]): country_id of the IdentificationtemplatesUpdateModel.

                - documents_footnote (str): documents_footnote of the IdentificationtemplatesUpdateModel.

                - email (str): email of the IdentificationtemplatesUpdateModel.

                - email_sender_address (str): email_sender_address of the IdentificationtemplatesUpdateModel.

                - email_sender_name (str): email_sender_name of the IdentificationtemplatesUpdateModel.

                - fax (str): fax of the IdentificationtemplatesUpdateModel.

                - name (str): name of the IdentificationtemplatesUpdateModel.

                - notes (str): notes of the IdentificationtemplatesUpdateModel.

                - phone (str): phone of the IdentificationtemplatesUpdateModel.

                - template_id (Union[str, int]): template_id of the IdentificationtemplatesUpdateModel.

                - website (str): website of the IdentificationtemplatesUpdateModel.

                - zip_code (str): zip_code of the IdentificationtemplatesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, IdentificationtemplatesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
