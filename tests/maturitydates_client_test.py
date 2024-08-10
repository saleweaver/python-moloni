import unittest
from unittest.mock import patch, Mock
from requests import Response
from moloni.api.maturitydates_client import (
    MaturitydatesClient,
    MaturitydatesCountModifiedSinceModel,
    MaturitydatesDeleteModel,
    MaturitydatesGetAllModel,
    MaturitydatesGetModifiedSinceModel,
    MaturitydatesInsertModel,
    MaturitydatesUpdateModel,
)
from moloni.base import ApiResponse, NoMoreRecords


class TestMaturitydatesClient(unittest.TestCase):
    def setUp(self):
        self.client = MaturitydatesClient()

    @patch.object(MaturitydatesClient, "_request")
    def test_count_modified_since(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = MaturitydatesCountModifiedSinceModel(
            company_id="sample_value",
            lastmodified="lastmodified",
        )
        response = self.client.count_modified_since(data=model_data)

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

    @patch.object(MaturitydatesClient, "_request")
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

        model_data = MaturitydatesDeleteModel(
            company_id="sample_value",
            maturity_date_id="sample_value",
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

    @patch.object(MaturitydatesClient, "_request")
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

        model_data = MaturitydatesGetAllModel(
            company_id="sample_value",
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

    @patch.object(MaturitydatesClient, "_request")
    def test_get_modified_since(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = MaturitydatesGetModifiedSinceModel(
            company_id="sample_value",
            lastmodified="lastmodified",
        )
        response = self.client.get_modified_since(data=model_data)

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

    @patch.object(MaturitydatesClient, "_request")
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

        model_data = MaturitydatesInsertModel(
            associated_discount="associated_discount",
            company_id="sample_value",
            days="days",
            name="name",
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

    @patch.object(MaturitydatesClient, "_request")
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

        model_data = MaturitydatesUpdateModel(
            associated_discount="associated_discount",
            company_id="sample_value",
            days="days",
            maturity_date_id="sample_value",
            name="name",
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
