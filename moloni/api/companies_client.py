from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class CompaniesGetOneModel(BaseModel):
    company_id: Union[str, int]


class CompaniesUpdateModel(BaseModel):
    company_id: Union[str, int]
    name: str
    address: str = None
    capital: str = None
    city: str = None
    commercial_registration_number: str = None
    country_id: Union[str, int] = None
    currency_id: Union[str, int] = None
    customer_series: str = None
    decimal_places: str = None
    decimal_separator: str = None
    delivery_method_id: Union[str, int] = None
    detached_series_doc_number: str = None
    docs_commercial_info_on_footer: str = None
    docs_company_info_position: str = None
    docs_copies: str = None
    docs_footer: str = None
    docs_pdf_model_id: Union[str, int] = None
    docs_qty_products_page: str = None
    docs_show_client_phone: str = None
    docs_show_client_vat_prefix: str = None
    docs_show_company_notes: str = None
    docs_show_related: str = None
    docs_show_values_on_movement_docs: str = None
    docs_show_values_on_return_docs: str = None
    docs_show_values_orders_docs: str = None
    docs_show_values_with_taxes: str = None
    email: str = None
    fax: str = None
    is_retailer_or_tsp: bool = None
    mails_sender_address: str = None
    mails_sender_name: str = None
    maturity_date_id: Union[str, int] = None
    maturity_on_week_day: str = None
    notes: str = None
    notify_late_documents: str = None
    numeric_code_ordering: str = None
    payment_method_id: Union[str, int] = None
    phone: str = None
    registry_office: str = None
    show_home_charts: str = None
    show_inactive_customers: str = None
    show_inactive_products: str = None
    thousands_separator: str = None
    vat: str = None
    website: str = None
    zip_code: str = None


class CompaniesClient(MoloniBaseClient):

    @endpoint("/<version>/companies/getAll/", method="post")
    def get_all(self, **kwargs):
        """
        get_all(self, **kwargs)

        Args:


        Returns:
            ApiResponse: The response from the API.
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**kwargs}
        )

    @endpoint("/<version>/companies/getOne/", method="post")
    def get_one(self, data: Union[CompaniesGetOneModel, dict], **kwargs):
        """
        get_one(self, data: Union[CompaniesGetOneModel, dict], **kwargs)

        Args:

            data (Union[CompaniesGetOneModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the CompaniesGetOneModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CompaniesGetOneModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/companies/update/", method="post")
    def update(self, data: Union[CompaniesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[CompaniesUpdateModel, dict], **kwargs)

        Args:

            data (Union[CompaniesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - address (str): address of the CompaniesUpdateModel.

                - capital (str): capital of the CompaniesUpdateModel.

                - city (str): city of the CompaniesUpdateModel.

                - commercial_registration_number (str): commercial_registration_number of the CompaniesUpdateModel.

                - company_id (Union[str, int]): company_id of the CompaniesUpdateModel.

                - country_id (Union[str, int]): country_id of the CompaniesUpdateModel.

                - currency_id (Union[str, int]): currency_id of the CompaniesUpdateModel.

                - customer_series (str): customer_series of the CompaniesUpdateModel.

                - decimal_places (str): decimal_places of the CompaniesUpdateModel.

                - decimal_separator (str): decimal_separator of the CompaniesUpdateModel.

                - delivery_method_id (Union[str, int]): delivery_method_id of the CompaniesUpdateModel.

                - detached_series_doc_number (str): detached_series_doc_number of the CompaniesUpdateModel.

                - docs_commercial_info_on_footer (str): docs_commercial_info_on_footer of the CompaniesUpdateModel.

                - docs_company_info_position (str): docs_company_info_position of the CompaniesUpdateModel.

                - docs_copies (str): docs_copies of the CompaniesUpdateModel.

                - docs_footer (str): docs_footer of the CompaniesUpdateModel.

                - docs_pdf_model_id (Union[str, int]): docs_pdf_model_id of the CompaniesUpdateModel.

                - docs_qty_products_page (str): docs_qty_products_page of the CompaniesUpdateModel.

                - docs_show_client_phone (str): docs_show_client_phone of the CompaniesUpdateModel.

                - docs_show_client_vat_prefix (str): docs_show_client_vat_prefix of the CompaniesUpdateModel.

                - docs_show_company_notes (str): docs_show_company_notes of the CompaniesUpdateModel.

                - docs_show_related (str): docs_show_related of the CompaniesUpdateModel.

                - docs_show_values_on_movement_docs (str): docs_show_values_on_movement_docs of the CompaniesUpdateModel.

                - docs_show_values_on_return_docs (str): docs_show_values_on_return_docs of the CompaniesUpdateModel.

                - docs_show_values_orders_docs (str): docs_show_values_orders_docs of the CompaniesUpdateModel.

                - docs_show_values_with_taxes (str): docs_show_values_with_taxes of the CompaniesUpdateModel.

                - email (str): email of the CompaniesUpdateModel.

                - fax (str): fax of the CompaniesUpdateModel.

                - is_retailer_or_tsp (bool): is_retailer_or_tsp of the CompaniesUpdateModel.

                - mails_sender_address (str): mails_sender_address of the CompaniesUpdateModel.

                - mails_sender_name (str): mails_sender_name of the CompaniesUpdateModel.

                - maturity_date_id (Union[str, int]): maturity_date_id of the CompaniesUpdateModel.

                - maturity_on_week_day (str): maturity_on_week_day of the CompaniesUpdateModel.

                - name (str): name of the CompaniesUpdateModel.

                - notes (str): notes of the CompaniesUpdateModel.

                - notify_late_documents (str): notify_late_documents of the CompaniesUpdateModel.

                - numeric_code_ordering (str): numeric_code_ordering of the CompaniesUpdateModel.

                - payment_method_id (Union[str, int]): payment_method_id of the CompaniesUpdateModel.

                - phone (str): phone of the CompaniesUpdateModel.

                - registry_office (str): registry_office of the CompaniesUpdateModel.

                - show_home_charts (str): show_home_charts of the CompaniesUpdateModel.

                - show_inactive_customers (str): show_inactive_customers of the CompaniesUpdateModel.

                - show_inactive_products (str): show_inactive_products of the CompaniesUpdateModel.

                - thousands_separator (str): thousands_separator of the CompaniesUpdateModel.

                - vat (str): vat of the CompaniesUpdateModel.

                - website (str): website of the CompaniesUpdateModel.

                - zip_code (str): zip_code of the CompaniesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, CompaniesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
