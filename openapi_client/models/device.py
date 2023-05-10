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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, conlist
from openapi_client.models.sensor import Sensor

class Device(BaseModel):
    """
    Device
    """
    id: Optional[Union[StrictFloat, StrictInt]] = None
    code: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    organisation: Optional[StrictStr] = None
    properties: Optional[Dict[str, Any]] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    location_description: Optional[StrictStr] = None
    sensors: Optional[conlist(Sensor)] = None
    __properties = ["id", "code", "description", "organisation", "properties", "latitude", "longitude", "location_description", "sensors"]

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
    def from_json(cls, json_str: str) -> Device:
        """Create an instance of Device from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in sensors (list)
        _items = []
        if self.sensors:
            for _item in self.sensors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sensors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Device:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Device.parse_obj(obj)

        _obj = Device.parse_obj({
            "id": obj.get("id"),
            "code": obj.get("code"),
            "description": obj.get("description"),
            "organisation": obj.get("organisation"),
            "properties": obj.get("properties"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "location_description": obj.get("location_description"),
            "sensors": [Sensor.from_dict(_item) for _item in obj.get("sensors")] if obj.get("sensors") is not None else None
        })
        return _obj

