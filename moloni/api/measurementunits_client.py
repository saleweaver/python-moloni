from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = MeasurementunitsClient(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class MeasurementunitsCountModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.count_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class MeasurementunitsDeleteModel(ApiRequestModel):
    company_id: Union[str, int]
    unit_id: Optional[Union[str, int]] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.delete(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class MeasurementunitsGetAllModel(ApiRequestModel):
    company_id: Union[str, int]

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_all(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class MeasurementunitsGetModifiedSinceModel(ApiRequestModel):
    company_id: Union[str, int]
    lastmodified: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.get_modified_since(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class MeasurementunitsInsertModel(ApiRequestModel):
    company_id: Union[str, int]
    name: Optional[str] = None
    short_name: Optional[str] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.insert(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class MeasurementunitsUpdateModel(ApiRequestModel):
    company_id: Union[str, int]
    name: Optional[str] = None
    short_name: Optional[str] = None
    unit_id: Optional[Union[str, int]] = None

    def request(self):
        if hasattr(self, "_api_client"):
            response = self._api_client.update(
                self.model_dump(exclude={"_api_client"}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")


class MeasurementunitsClient(MoloniBaseClient):

    @endpoint("/<version>/measurementUnits/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[MeasurementunitsCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[MeasurementunitsCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[MeasurementunitsCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MeasurementunitsCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the MeasurementunitsCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(
            data, self.validate, MeasurementunitsCountModifiedSinceModel
        )

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/measurementUnits/delete/", method="post")
    def delete(self, data: Union[MeasurementunitsDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[MeasurementunitsDeleteModel, dict], **kwargs)

        Args:

            data (Union[MeasurementunitsDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MeasurementunitsDeleteModel.

                - unit_id (Union[str, int]): unit_id of the MeasurementunitsDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MeasurementunitsDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/measurementUnits/getAll/", method="post")
    def get_all(self, data: Union[MeasurementunitsGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[MeasurementunitsGetAllModel, dict], **kwargs)

        Args:

            data (Union[MeasurementunitsGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MeasurementunitsGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MeasurementunitsGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/measurementUnits/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[MeasurementunitsGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[MeasurementunitsGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[MeasurementunitsGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MeasurementunitsGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the MeasurementunitsGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MeasurementunitsGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/measurementUnits/insert/", method="post")
    def insert(self, data: Union[MeasurementunitsInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[MeasurementunitsInsertModel, dict], **kwargs)

        Args:

            data (Union[MeasurementunitsInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MeasurementunitsInsertModel.

                - name (str): name of the MeasurementunitsInsertModel.

                - short_name (str): short_name of the MeasurementunitsInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MeasurementunitsInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/measurementUnits/update/", method="post")
    def update(self, data: Union[MeasurementunitsUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[MeasurementunitsUpdateModel, dict], **kwargs)

        Args:

            data (Union[MeasurementunitsUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the MeasurementunitsUpdateModel.

                - name (str): name of the MeasurementunitsUpdateModel.

                - short_name (str): short_name of the MeasurementunitsUpdateModel.

                - unit_id (Union[str, int]): unit_id of the MeasurementunitsUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, MeasurementunitsUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
