# coding: utf-8

"""
    Sensorbucket API

    SensorBucket processes data from different sources and devices into a single standardized format.  An applications connected to SensorBucket, can use all devices SensorBucket supports.  Missing a device or source? SensorBucket is designed to be scalable and extendable. Create your own worker that receives data from an AMQP source, process said data and output in the expected worker output format.  Find out more at: https://developer.sensorbucket.nl/  Developed and designed by Provincie Zeeland and Pollex' 

    The version of the OpenAPI document: 1.2.0-rc1
    Contact: info@pollex.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from sensorbucket.models.sensor import Sensor
from typing import Optional, Set
from typing_extensions import Self

class Device(BaseModel):
    """
    Device
    """ # noqa: E501
    id: StrictInt
    code: StrictStr
    state: StrictInt
    description: StrictStr
    organisation: StrictStr
    properties: Dict[str, Any]
    altitude: Optional[Union[StrictFloat, StrictInt]] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    location_description: Optional[StrictStr] = None
    sensors: List[Sensor]
    created_at: datetime
    __properties: ClassVar[List[str]] = ["id", "code", "state", "description", "organisation", "properties", "altitude", "latitude", "longitude", "location_description", "sensors", "created_at"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Device from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in sensors (list)
        _items = []
        if self.sensors:
            for _item in self.sensors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sensors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "code": obj.get("code"),
            "state": obj.get("state"),
            "description": obj.get("description"),
            "organisation": obj.get("organisation"),
            "properties": obj.get("properties"),
            "altitude": obj.get("altitude"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "location_description": obj.get("location_description"),
            "sensors": [Sensor.from_dict(_item) for _item in obj["sensors"]] if obj.get("sensors") is not None else None,
            "created_at": obj.get("created_at")
        })
        return _obj


