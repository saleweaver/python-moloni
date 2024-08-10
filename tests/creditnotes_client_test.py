import unittest
from unittest.mock import patch, Mock
from requests import Response
from moloni.api.creditnotes_client import (
    CreditnotesClient,
    CreditnotesCountModel,
    CreditnotesDeleteModel,
    CreditnotesGetAllModel,
    CreditnotesGetOneModel,
    CreditnotesInsertModel,
    CreditnotesUpdateModel,
)
from moloni.base import ApiResponse, NoMoreRecords


class TestCreditnotesClient(unittest.TestCase):
    def setUp(self):
        self.client = CreditnotesClient()

    @patch.object(CreditnotesClient, "_request")
    def test_count(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = CreditnotesCountModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            our_reference="our_reference",
            salesman_id="sample_value",
            supplier_id="sample_value",
            year="year",
            your_reference="your_reference",
        )
        response = self.client.count(data=model_data)

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

    @patch.object(CreditnotesClient, "_request")
    def test_delete(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = CreditnotesDeleteModel(
            company_id="sample_value",
            document_id="sample_value",
        )
        response = self.client.delete(data=model_data)

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

    @patch.object(CreditnotesClient, "_request")
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

        model_data = CreditnotesGetAllModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            offset="offset",
            our_reference="our_reference",
            qty="qty",
            salesman_id="sample_value",
            supplier_id="sample_value",
            year="year",
            your_reference="your_reference",
        )
        response = self.client.get_all(data=model_data)

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

    @patch.object(CreditnotesClient, "_request")
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

        model_data = CreditnotesGetOneModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_id="sample_value",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            our_reference="our_reference",
            salesman_id="sample_value",
            supplier_id="sample_value",
            year="year",
            your_reference="your_reference",
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

    @patch.object(CreditnotesClient, "_request")
    def test_insert(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = CreditnotesInsertModel(
            associated_documents=[],
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            deduction_id="sample_value",
            document_set_id="sample_value",
            financial_discount="financial_discount",
            notes="notes",
            products=[],
            related_documents_notes="related_documents_notes",
            salesman_commission="salesman_commission",
            salesman_id="sample_value",
            status="status",
            your_reference="your_reference",
        )
        response = self.client.insert(data=model_data)

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

    @patch.object(CreditnotesClient, "_request")
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

        model_data = CreditnotesUpdateModel(
            associated_documents=[],
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            deduction_id="sample_value",
            document_id="sample_value",
            document_set_id="sample_value",
            financial_discount="financial_discount",
            notes="notes",
            products=[],
            related_documents_notes="related_documents_notes",
            salesman_commission="salesman_commission",
            salesman_id="sample_value",
            status="status",
            your_reference="your_reference",
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
