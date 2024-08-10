import functools
import re
from urllib import parse

from pydantic import BaseModel
from pydantic import ValidationError
from requests import Response


def fill_query_params(query, version, *args):
    return re.sub(
        "<version>", version, query.format(*[parse.quote(arg, safe="") for arg in args])
    )


def endpoint(path, method="POST"):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            kwargs.update({"path": path, "method": method})
            return function(*args, **kwargs)

        return wrapper

    return decorator


def validate_data(data, validate, model):
    if isinstance(data, dict):
        if validate:
            try:
                model = model(**data)
                data = model.model_dump(exclude_unset=True)
            except ValidationError as e:
                raise e
        # No else needed here because we want to use the dict directly if validate is False
    elif isinstance(data, BaseModel):
        data = data.model_dump(exclude_unset=True)

    return data


class AccessTokenResponse:
    def __init__(self, **kwargs):
        self.access_token = kwargs.get("access_token")
        self.refresh_token = kwargs.get("refresh_token")
        self.expires_in = kwargs.get("expires_in")
        self.token_type = kwargs.get("token_type")

    def dict(self):
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_in": self.expires_in,
            "token_type": self.token_type,
        }


class NoMoreRecords(Exception):
    pass


class ApiException(Exception):
    def __init__(self, response: Response, request_data: dict, **kwargs):
        self.error = response.json()
        self.status_code = response.status_code
        self.headers = response.headers
        self.kwargs = kwargs
        self.request_data = request_data

    def __str__(self):
        return f"ApiException(error={self.error}, status_code={self.status_code}, headers={self.headers}, kwargs={self.kwargs}, request_data={self.request_data})"


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

    def __str__(self):
        return f"ApiResponse(payload={self.payload}, qty={self.qty}, requested_qty={self.requested_qty}, has_more={self.has_more}, offset={self.offset}, status_code={self.status_code}, headers={self.headers}, kwargs={self.kwargs})"
