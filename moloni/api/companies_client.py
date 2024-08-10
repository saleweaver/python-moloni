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


class CompaniesGetOneModel(BaseModel):
    company_id: Union[str, int]


class CompaniesUpdateModel(BaseModel):
    company_id: Union[str, int]
    address: Optional[str] = None
    capital: Optional[str] = None
    city: Optional[str] = None
    commercial_registration_number: Optional[str] = None
    country_id: Optional[Union[str, int]] = None
    currency_id: Optional[Union[str, int]] = None
    customer_series: Optional[str] = None
    decimal_places: Optional[str] = None
    decimal_separator: Optional[str] = None
    delivery_method_id: Optional[Union[str, int]] = None
    detached_series_doc_number: Optional[str] = None
    docs_commercial_info_on_footer: Optional[str] = None
    docs_company_info_position: Optional[str] = None
    docs_copies: Optional[str] = None
    docs_footer: Optional[str] = None
    docs_pdf_model_id: Optional[Union[str, int]] = None
    docs_qty_products_page: Optional[str] = None
    docs_show_client_phone: Optional[str] = None
    docs_show_client_vat_prefix: Optional[str] = None
    docs_show_company_notes: Optional[str] = None
    docs_show_related: Optional[str] = None
    docs_show_values_on_movement_docs: Optional[str] = None
    docs_show_values_on_return_docs: Optional[str] = None
    docs_show_values_orders_docs: Optional[str] = None
    docs_show_values_with_taxes: Optional[str] = None
    email: Optional[str] = None
    fax: Optional[str] = None
    is_retailer_or_tsp: Optional[bool] = None
    mails_sender_address: Optional[str] = None
    mails_sender_name: Optional[str] = None
    maturity_date_id: Optional[Union[str, int]] = None
    maturity_on_week_day: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    notify_late_documents: Optional[str] = None
    numeric_code_ordering: Optional[str] = None
    payment_method_id: Optional[Union[str, int]] = None
    phone: Optional[str] = None
    registry_office: Optional[str] = None
    show_home_charts: Optional[str] = None
    show_inactive_customers: Optional[str] = None
    show_inactive_products: Optional[str] = None
    thousands_separator: Optional[str] = None
    vat: Optional[str] = None
    website: Optional[str] = None
    zip_code: Optional[str] = None


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
