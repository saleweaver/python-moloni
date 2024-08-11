import unittest
from unittest.mock import patch, Mock
from requests import Response
from moloni.api.companies_client import (
    CompaniesClient,
    CompaniesGetOneModel,
    CompaniesUpdateModel,
)
from moloni.base import ApiResponse, NoMoreRecords


class TestCompaniesClient(unittest.TestCase):
    def setUp(self):
        self.client = CompaniesClient()

    @patch.object(CompaniesClient, "_request")
    def test_get_all(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        response = self.client.get_all()

        # Assertions
        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.payload, {"some_key": "some_value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        mock_request.assert_called_once()

        # Test pagination functionality
        try:
            next_params = response.next(qty=5)
            self.assertEqual(next_params["offset"], 10)
            self.assertEqual(next_params["qty"], 5)
        except NoMoreRecords:
            pass

    @patch.object(CompaniesClient, "_request")
    def test_get_one(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = CompaniesGetOneModel(
            company_id="sample_value",
        )
        response = self.client.get_one(data=model_data)

        # Assertions
        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.payload, {"some_key": "some_value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        mock_request.assert_called_once()

        # Test pagination functionality
        try:
            next_params = response.next(qty=5)
            self.assertEqual(next_params["offset"], 10)
            self.assertEqual(next_params["qty"], 5)
        except NoMoreRecords:
            pass

    @patch.object(CompaniesClient, "_request")
    def test_get_one_from_model(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = CompaniesGetOneModel(
            company_id="sample_value",
        )
        with model_data.connect() as api:
            response = api.request()

        # Assertions
        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.payload, {"some_key": "some_value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        mock_request.assert_called_once()

        # Test pagination functionality
        try:
            next_params = response.next(qty=5)
            self.assertEqual(next_params["offset"], 10)
            self.assertEqual(next_params["qty"], 5)
        except NoMoreRecords:
            pass

    @patch.object(CompaniesClient, "_request")
    def test_update(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = CompaniesUpdateModel(
            address="address",
            capital="capital",
            city="city",
            commercial_registration_number="commercial_registration_number",
            company_id="sample_value",
            country_id="sample_value",
            currency_id="sample_value",
            customer_series="customer_series",
            decimal_places="decimal_places",
            decimal_separator="decimal_separator",
            delivery_method_id="sample_value",
            detached_series_doc_number="detached_series_doc_number",
            docs_commercial_info_on_footer="docs_commercial_info_on_footer",
            docs_company_info_position="docs_company_info_position",
            docs_copies="docs_copies",
            docs_footer="docs_footer",
            docs_pdf_model_id="sample_value",
            docs_qty_products_page="docs_qty_products_page",
            docs_show_client_phone="docs_show_client_phone",
            docs_show_client_vat_prefix="docs_show_client_vat_prefix",
            docs_show_company_notes="docs_show_company_notes",
            docs_show_related="docs_show_related",
            docs_show_values_on_movement_docs="docs_show_values_on_movement_docs",
            docs_show_values_on_return_docs="docs_show_values_on_return_docs",
            docs_show_values_orders_docs="docs_show_values_orders_docs",
            docs_show_values_with_taxes="docs_show_values_with_taxes",
            email="email",
            fax="fax",
            is_retailer_or_tsp=True,
            mails_sender_address="mails_sender_address",
            mails_sender_name="mails_sender_name",
            maturity_date_id="sample_value",
            maturity_on_week_day="maturity_on_week_day",
            name="name",
            notes="notes",
            notify_late_documents="notify_late_documents",
            numeric_code_ordering="numeric_code_ordering",
            payment_method_id="sample_value",
            phone="phone",
            registry_office="registry_office",
            show_home_charts="show_home_charts",
            show_inactive_customers="show_inactive_customers",
            show_inactive_products="show_inactive_products",
            thousands_separator="thousands_separator",
            vat="vat",
            website="website",
            zip_code="zip_code",
        )
        response = self.client.update(data=model_data)

        # Assertions
        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.payload, {"some_key": "some_value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        mock_request.assert_called_once()

        # Test pagination functionality
        try:
            next_params = response.next(qty=5)
            self.assertEqual(next_params["offset"], 10)
            self.assertEqual(next_params["qty"], 5)
        except NoMoreRecords:
            pass

    @patch.object(CompaniesClient, "_request")
    def test_update_from_model(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = CompaniesUpdateModel(
            address="address",
            capital="capital",
            city="city",
            commercial_registration_number="commercial_registration_number",
            company_id="sample_value",
            country_id="sample_value",
            currency_id="sample_value",
            customer_series="customer_series",
            decimal_places="decimal_places",
            decimal_separator="decimal_separator",
            delivery_method_id="sample_value",
            detached_series_doc_number="detached_series_doc_number",
            docs_commercial_info_on_footer="docs_commercial_info_on_footer",
            docs_company_info_position="docs_company_info_position",
            docs_copies="docs_copies",
            docs_footer="docs_footer",
            docs_pdf_model_id="sample_value",
            docs_qty_products_page="docs_qty_products_page",
            docs_show_client_phone="docs_show_client_phone",
            docs_show_client_vat_prefix="docs_show_client_vat_prefix",
            docs_show_company_notes="docs_show_company_notes",
            docs_show_related="docs_show_related",
            docs_show_values_on_movement_docs="docs_show_values_on_movement_docs",
            docs_show_values_on_return_docs="docs_show_values_on_return_docs",
            docs_show_values_orders_docs="docs_show_values_orders_docs",
            docs_show_values_with_taxes="docs_show_values_with_taxes",
            email="email",
            fax="fax",
            is_retailer_or_tsp=True,
            mails_sender_address="mails_sender_address",
            mails_sender_name="mails_sender_name",
            maturity_date_id="sample_value",
            maturity_on_week_day="maturity_on_week_day",
            name="name",
            notes="notes",
            notify_late_documents="notify_late_documents",
            numeric_code_ordering="numeric_code_ordering",
            payment_method_id="sample_value",
            phone="phone",
            registry_office="registry_office",
            show_home_charts="show_home_charts",
            show_inactive_customers="show_inactive_customers",
            show_inactive_products="show_inactive_products",
            thousands_separator="thousands_separator",
            vat="vat",
            website="website",
            zip_code="zip_code",
        )
        with model_data.connect() as api:
            response = api.request()

        # Assertions
        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.payload, {"some_key": "some_value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        mock_request.assert_called_once()

        # Test pagination functionality
        try:
            next_params = response.next(qty=5)
            self.assertEqual(next_params["offset"], 10)
            self.assertEqual(next_params["qty"], 5)
        except NoMoreRecords:
            pass
