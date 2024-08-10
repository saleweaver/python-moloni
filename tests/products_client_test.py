import unittest
from unittest.mock import patch, Mock
from requests import Response
from moloni.api.products_client import (
    ProductsClient,
    ProductsCountModel,
    ProductsCountByEanModel,
    ProductsCountByNameModel,
    ProductsCountByReferenceModel,
    ProductsCountBySearchModel,
    ProductsCountModifiedSinceModel,
    ProductsDeleteModel,
    ProductsGetAllModel,
    ProductsGetByEanModel,
    ProductsGetByNameModel,
    ProductsGetByReferenceModel,
    ProductsGetBySearchModel,
    ProductsGetModifiedSinceModel,
    ProductsGetOneModel,
    ProductsInsertModel,
    ProductsUpdateModel,
)
from moloni.base import ApiResponse, NoMoreRecords


class TestProductsClient(unittest.TestCase):
    def setUp(self):
        self.client = ProductsClient()

    @patch.object(ProductsClient, "_request")
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

        model_data = ProductsCountModel(
            category_id="sample_value",
            company_id="sample_value",
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

    @patch.object(ProductsClient, "_request")
    def test_count_by_ean(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = ProductsCountByEanModel(
            company_id="sample_value",
            ean="ean",
        )
        response = self.client.count_by_ean(data=model_data)

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

    @patch.object(ProductsClient, "_request")
    def test_count_by_name(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = ProductsCountByNameModel(
            company_id="sample_value",
            name="name",
        )
        response = self.client.count_by_name(data=model_data)

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

    @patch.object(ProductsClient, "_request")
    def test_count_by_reference(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = ProductsCountByReferenceModel(
            company_id="sample_value",
            reference="reference",
        )
        response = self.client.count_by_reference(data=model_data)

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

    @patch.object(ProductsClient, "_request")
    def test_count_by_search(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = ProductsCountBySearchModel(
            company_id="sample_value",
            search="search",
        )
        response = self.client.count_by_search(data=model_data)

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

    @patch.object(ProductsClient, "_request")
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

        model_data = ProductsCountModifiedSinceModel(
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

    @patch.object(ProductsClient, "_request")
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

        model_data = ProductsDeleteModel(
            company_id="sample_value",
            product_id="sample_value",
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

    @patch.object(ProductsClient, "_request")
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

        model_data = ProductsGetAllModel(
            category_id="sample_value",
            company_id="sample_value",
            offset="offset",
            qty="qty",
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

    @patch.object(ProductsClient, "_request")
    def test_get_by_ean(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = ProductsGetByEanModel(
            company_id="sample_value",
            ean="ean",
            offset="offset",
            qty="qty",
        )
        response = self.client.get_by_ean(data=model_data)

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

    @patch.object(ProductsClient, "_request")
    def test_get_by_name(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = ProductsGetByNameModel(
            company_id="sample_value",
            name="name",
            offset="offset",
            qty="qty",
        )
        response = self.client.get_by_name(data=model_data)

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

    @patch.object(ProductsClient, "_request")
    def test_get_by_reference(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = ProductsGetByReferenceModel(
            company_id="sample_value",
            offset="offset",
            qty="qty",
            reference="reference",
        )
        response = self.client.get_by_reference(data=model_data)

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

    @patch.object(ProductsClient, "_request")
    def test_get_by_search(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response, request_data={"qty": 10, "offset": 0}
        )

        model_data = ProductsGetBySearchModel(
            company_id="sample_value",
            offset="offset",
            qty="qty",
            search="search",
        )
        response = self.client.get_by_search(data=model_data)

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

    @patch.object(ProductsClient, "_request")
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

        model_data = ProductsGetModifiedSinceModel(
            company_id="sample_value",
            lastmodified="lastmodified",
            offset="offset",
            qty="qty",
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

    @patch.object(ProductsClient, "_request")
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

        model_data = ProductsGetOneModel(
            company_id="sample_value",
            product_id="sample_value",
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

    @patch.object(ProductsClient, "_request")
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

        model_data = ProductsInsertModel(
            at_product_category="at_product_category",
            category_id="sample_value",
            company_id="sample_value",
            ean="ean",
            exemption_reason="exemption_reason",
            has_stock="has_stock",
            name="name",
            pos_favorite="pos_favorite",
            price="price",
            reference="reference",
            stock="stock",
            summary="summary",
            suppliers=[],
            taxes=[],
            type="type",
            unit_id="sample_value",
            warehouse_id="sample_value",
            warehouses=[],
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

    @patch.object(ProductsClient, "_request")
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

        model_data = ProductsUpdateModel(
            at_product_category="at_product_category",
            category_id="sample_value",
            company_id="sample_value",
            ean="ean",
            exemption_reason="exemption_reason",
            has_stock="has_stock",
            name="name",
            pos_favorite="pos_favorite",
            price="price",
            product_id="sample_value",
            reference="reference",
            stock="stock",
            summary="summary",
            suppliers=[],
            taxes=[],
            type="type",
            unit_id="sample_value",
            warehouse_id="sample_value",
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
