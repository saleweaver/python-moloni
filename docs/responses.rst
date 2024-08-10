Responses
=========

All endpoints return `moloni.base.ApiResponse` with the following signature. `payload` contains Moloni's response.

.. code-block:: python

    from moloni.base import ApiResponse

    class ApiResponse:
        def __init__(self, response: Response, request_data: dict, **kwargs):
            self.payload = response.json()
            self.qty = len(self.payload)
            self.requested_qty = request_data.get("qty", None)
            self.has_more = self.qty == self.requested_qty
            self.offset = request_data.get("offset", None)
            self.status_code = response.status_code
            self.headers = response.headers
            self.kwargs = kwargs

        def next(self, qty=None):
            """Get the next page for methods that return paginated responses"""
            if not self.has_more:
                raise NoMoreRecords("No more records to fetch")
            return {
                "offset": self.offset + self.requested_qty,
                "qty": qty or self.requested_qty,
            }



-----------------------------------------

..  autoclass:: moloni.base.ApiResponse


