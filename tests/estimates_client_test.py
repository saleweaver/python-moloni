import unittest
from unittest.mock import patch, Mock
from requests import Response
from moloni.api.estimates_client import (
    EstimatesClient,
    EstimatesCountModel,
    EstimatesDeleteModel,
    EstimatesGetAllModel,
    EstimatesGetOneModel,
    EstimatesInsertModel,
    EstimatesUpdateModel,
)
from moloni.base import ApiResponse, NoMoreRecords


class TestEstimatesClient(unittest.TestCase):
    def setUp(self):
        self.client = EstimatesClient()

    @patch.object(EstimatesClient, "_request")
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

        model_data = EstimatesCountModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            salesman_id="sample_value",
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

    @patch.object(EstimatesClient, "_request")
    def test_count_from_model(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = EstimatesCountModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            salesman_id="sample_value",
            year="year",
            your_reference="your_reference",
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

    @patch.object(EstimatesClient, "_request")
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

        model_data = EstimatesDeleteModel(
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

    @patch.object(EstimatesClient, "_request")
    def test_delete_from_model(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = EstimatesDeleteModel(
            company_id="sample_value",
            document_id="sample_value",
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

    @patch.object(EstimatesClient, "_request")
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

        model_data = EstimatesGetAllModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            offset="offset",
            qty="qty",
            salesman_id="sample_value",
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

    @patch.object(EstimatesClient, "_request")
    def test_get_all_from_model(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = EstimatesGetAllModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            offset="offset",
            qty="qty",
            salesman_id="sample_value",
            year="year",
            your_reference="your_reference",
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

    @patch.object(EstimatesClient, "_request")
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

        model_data = EstimatesGetOneModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_id="sample_value",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            salesman_id="sample_value",
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

    @patch.object(EstimatesClient, "_request")
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

        model_data = EstimatesGetOneModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            document_id="sample_value",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            number="number",
            salesman_id="sample_value",
            year="year",
            your_reference="your_reference",
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

    @patch.object(EstimatesClient, "_request")
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

        model_data = EstimatesInsertModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            deduction_id="sample_value",
            delivery_datetime="delivery_datetime",
            delivery_departure_address="delivery_departure_address",
            delivery_departure_city="delivery_departure_city",
            delivery_departure_country="delivery_departure_country",
            delivery_departure_zip_code="delivery_departure_zip_code",
            delivery_destination_address="delivery_destination_address",
            delivery_destination_city="delivery_destination_city",
            delivery_destination_country="delivery_destination_country",
            delivery_destination_zip_code="delivery_destination_zip_code",
            delivery_method_id="sample_value",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            financial_discount="financial_discount",
            notes="notes",
            products=[],
            salesman_commission="salesman_commission",
            salesman_id="sample_value",
            special_discount="special_discount",
            status="status",
            vehicle_id="sample_value",
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

    @patch.object(EstimatesClient, "_request")
    def test_insert_from_model(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = EstimatesInsertModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            deduction_id="sample_value",
            delivery_datetime="delivery_datetime",
            delivery_departure_address="delivery_departure_address",
            delivery_departure_city="delivery_departure_city",
            delivery_departure_country="delivery_departure_country",
            delivery_departure_zip_code="delivery_departure_zip_code",
            delivery_destination_address="delivery_destination_address",
            delivery_destination_city="delivery_destination_city",
            delivery_destination_country="delivery_destination_country",
            delivery_destination_zip_code="delivery_destination_zip_code",
            delivery_method_id="sample_value",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            financial_discount="financial_discount",
            notes="notes",
            products=[],
            salesman_commission="salesman_commission",
            salesman_id="sample_value",
            special_discount="special_discount",
            status="status",
            vehicle_id="sample_value",
            your_reference="your_reference",
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

    @patch.object(EstimatesClient, "_request")
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

        model_data = EstimatesUpdateModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            deduction_id="sample_value",
            delivery_datetime="delivery_datetime",
            delivery_departure_address="delivery_departure_address",
            delivery_departure_city="delivery_departure_city",
            delivery_departure_country="delivery_departure_country",
            delivery_departure_zip_code="delivery_departure_zip_code",
            delivery_destination_address="delivery_destination_address",
            delivery_destination_city="delivery_destination_city",
            delivery_destination_country="delivery_destination_country",
            delivery_destination_zip_code="delivery_destination_zip_code",
            delivery_method_id="sample_value",
            document_id="sample_value",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            financial_discount="financial_discount",
            notes="notes",
            products=[],
            salesman_commission="salesman_commission",
            salesman_id="sample_value",
            special_discount="special_discount",
            status="status",
            vehicle_id="sample_value",
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

    @patch.object(EstimatesClient, "_request")
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

        model_data = EstimatesUpdateModel(
            company_id="sample_value",
            customer_id="sample_value",
            date="date",
            deduction_id="sample_value",
            delivery_datetime="delivery_datetime",
            delivery_departure_address="delivery_departure_address",
            delivery_departure_city="delivery_departure_city",
            delivery_departure_country="delivery_departure_country",
            delivery_departure_zip_code="delivery_departure_zip_code",
            delivery_destination_address="delivery_destination_address",
            delivery_destination_city="delivery_destination_city",
            delivery_destination_country="delivery_destination_country",
            delivery_destination_zip_code="delivery_destination_zip_code",
            delivery_method_id="sample_value",
            document_id="sample_value",
            document_set_id="sample_value",
            expiration_date="expiration_date",
            financial_discount="financial_discount",
            notes="notes",
            products=[],
            salesman_commission="salesman_commission",
            salesman_id="sample_value",
            special_discount="special_discount",
            status="status",
            vehicle_id="sample_value",
            your_reference="your_reference",
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
