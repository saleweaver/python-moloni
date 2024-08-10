import os

from cachetools import TTLCache
from pydantic import BaseModel
from requests import request

from moloni import __version__
from moloni.base.config import MoloniBaseUrl
from moloni.base.helpers import AccessTokenResponse, ApiResponse, ApiException
from .logger_config import setup_logger

logger = setup_logger(__name__)

cache = TTLCache(maxsize=10, ttl=3600)


class MyAuth:
    headers = {
        "Accept": "application/json",
        "User-Agent": f"python-moloni/{__version__}",
    }

    def __init__(
        self,
        environment: MoloniBaseUrl,
        client_id: str,
        client_secret: str,
        refresh_token: str = None,
        username: str = None,
        password: str = None,
    ):
        self.base_url = environment.value
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password

    def get_auth(self) -> AccessTokenResponse:
        """
        Get's the access token
        :return:AccessTokenResponse
        """

        cache_key = "token"
        try:
            access_token = cache[cache_key]
        except KeyError:
            access_token = self.get_token().dict()
            cache[cache_key] = access_token
        return AccessTokenResponse(**access_token)

    def get_token(self, **kwargs) -> AccessTokenResponse:
        if self.refresh_token:
            kwargs.update(
                dict(
                    client_id=self.client_id,
                    client_secret=self.client_secret,
                    grant_type="refresh_token",
                    refresh_token=self.refresh_token,
                )
            )
        else:
            kwargs.update(
                dict(
                    client_id=self.client_id,
                    client_secret=self.client_secret,
                    grant_type="password",
                    username=self.username,
                    password=self.password,
                )
            )
        return AccessTokenResponse(
            **request(
                method="GET",
                url=self.base_url + "/v1/grant",
                headers=self.headers,
                params=kwargs,
            ).json()
        )

    def __call__(self):
        auth = self.get_auth()
        return f"{auth.access_token}"


class AuthConfig(BaseModel):
    client_id: str = os.getenv("MOLONI_CLIENT_ID")
    client_secret: str = os.getenv("MOLONI_CLIENT_SECRET")
    refresh_token: str = os.getenv("MOLONI_REFRESH_TOKEN")
    username: str = os.getenv("MOLONI_USERNAME")
    password: str = os.getenv("MOLONI_PASSWORD")

    def __init__(self, **kwargs):
        # Update with passed parameters, which will override the defaults from env vars
        super().__init__(**{k: v for k, v in kwargs.items() if v is not None})


class MoloniBaseClient:
    headers = {
        "Accept": "application/json",
        "User-Agent": f"python-moloni/{__version__}",
    }

    def __init__(
        self,
        environment: MoloniBaseUrl = MoloniBaseUrl.PROD,
        *,
        auth_config: AuthConfig = AuthConfig(),
        version: str = "v1",
        validate: bool = True,
        log_level: str = "INFO",
    ):
        self.base_url = environment.value
        self.validate = validate
        self.version = version
        self.auth = MyAuth(
            environment,
            auth_config.client_id,
            auth_config.client_secret,
            auth_config.refresh_token,
            auth_config.username,
            auth_config.password,
        )
        logger.setLevel(log_level)

    def _request(self, path, data=None, **kwargs) -> ApiResponse:
        data = data or {}

        logger.debug(data)

        res = request(
            method=data.pop("method"),
            url=f"{self.base_url}{path}",
            headers=self.headers,
            params={"access_token": self.auth()},
            data=data,
        )
        logger.debug(res)
        logger.debug(res.request.url)
        logger.debug(res.content)

        if 200 <= res.status_code < 300:
            return ApiResponse(res, data)
        raise ApiException(res, data)
