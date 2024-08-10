from pydantic import BaseModel, ValidationError
from typing import Union

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


class VehiclesCountModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class VehiclesDeleteModel(BaseModel):
    company_id: Union[str, int]
    vehicle_id: Union[str, int]


class VehiclesGetAllModel(BaseModel):
    company_id: Union[str, int]


class VehiclesGetModifiedSinceModel(BaseModel):
    company_id: Union[str, int]
    lastmodified: str


class VehiclesInsertModel(BaseModel):
    company_id: Union[str, int]
    description: str
    number_plate: str


class VehiclesUpdateModel(BaseModel):
    company_id: Union[str, int]
    vehicle_id: Union[str, int]
    description: str = None
    number_plate: str = None


class VehiclesClient(MoloniBaseClient):

    @endpoint("/<version>/vehicles/countModifiedSince/", method="post")
    def count_modified_since(
        self, data: Union[VehiclesCountModifiedSinceModel, dict], **kwargs
    ):
        """
        count_modified_since(self, data: Union[VehiclesCountModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[VehiclesCountModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the VehiclesCountModifiedSinceModel.

                - lastmodified (str): lastmodified of the VehiclesCountModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, VehiclesCountModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/vehicles/delete/", method="post")
    def delete(self, data: Union[VehiclesDeleteModel, dict], **kwargs):
        """
        delete(self, data: Union[VehiclesDeleteModel, dict], **kwargs)

        Args:

            data (Union[VehiclesDeleteModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the VehiclesDeleteModel.

                - vehicle_id (Union[str, int]): vehicle_id of the VehiclesDeleteModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, VehiclesDeleteModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/vehicles/getAll/", method="post")
    def get_all(self, data: Union[VehiclesGetAllModel, dict], **kwargs):
        """
        get_all(self, data: Union[VehiclesGetAllModel, dict], **kwargs)

        Args:

            data (Union[VehiclesGetAllModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the VehiclesGetAllModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, VehiclesGetAllModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/vehicles/getModifiedSince/", method="post")
    def get_modified_since(
        self, data: Union[VehiclesGetModifiedSinceModel, dict], **kwargs
    ):
        """
        get_modified_since(self, data: Union[VehiclesGetModifiedSinceModel, dict], **kwargs)

        Args:

            data (Union[VehiclesGetModifiedSinceModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the VehiclesGetModifiedSinceModel.

                - lastmodified (str): lastmodified of the VehiclesGetModifiedSinceModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, VehiclesGetModifiedSinceModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/vehicles/insert/", method="post")
    def insert(self, data: Union[VehiclesInsertModel, dict], **kwargs):
        """
        insert(self, data: Union[VehiclesInsertModel, dict], **kwargs)

        Args:

            data (Union[VehiclesInsertModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the VehiclesInsertModel.

                - description (str): description of the VehiclesInsertModel.

                - number_plate (str): number_plate of the VehiclesInsertModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, VehiclesInsertModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )

    @endpoint("/<version>/vehicles/update/", method="post")
    def update(self, data: Union[VehiclesUpdateModel, dict], **kwargs):
        """
        update(self, data: Union[VehiclesUpdateModel, dict], **kwargs)

        Args:

            data (Union[VehiclesUpdateModel, dict]): A model instance or dictionary containing the following fields:

                - company_id (Union[str, int]): company_id of the VehiclesUpdateModel.

                - description (str): description of the VehiclesUpdateModel.

                - number_plate (str): number_plate of the VehiclesUpdateModel.

                - vehicle_id (Union[str, int]): vehicle_id of the VehiclesUpdateModel.



        Returns:
            ApiResponse: The response from the API.
        """

        data = validate_data(data, self.validate, VehiclesUpdateModel)

        return self._request(
            fill_query_params(kwargs.pop("path"), self.version), data={**data, **kwargs}
        )
