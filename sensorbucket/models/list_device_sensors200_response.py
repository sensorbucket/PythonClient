# coding: utf-8

"""
    Sensorbucket API

    SensorBucket processes data from different sources and devices into a single standardized format.  An applications connected to SensorBucket, can use all devices SensorBucket supports.  Missing a device or source? SensorBucket is designed to be scalable and extendable. Create your own worker that receives data from an AMQP source, process said data and output in the expected worker output format.  Find out more at: https://developer.sensorbucket.nl/  Developed and designed by Provincie Zeeland and Pollex   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: info@pollex.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from sensorbucket.models.paginated_response_links import PaginatedResponseLinks
from sensorbucket.models.sensor import Sensor

class ListDeviceSensors200Response(BaseModel):
    """
    ListDeviceSensors200Response
    """
    links: PaginatedResponseLinks = Field(...)
    page_size: StrictInt = Field(...)
    total_count: StrictInt = Field(...)
    data: conlist(Sensor) = Field(...)
    __properties = ["links", "page_size", "total_count", "data"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ListDeviceSensors200Response:
        """Create an instance of ListDeviceSensors200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListDeviceSensors200Response:
        """Create an instance of ListDeviceSensors200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListDeviceSensors200Response.parse_obj(obj)

        _obj = ListDeviceSensors200Response.parse_obj({
            "links": PaginatedResponseLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "page_size": obj.get("page_size"),
            "total_count": obj.get("total_count"),
            "data": [Sensor.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None
        })
        return _obj

