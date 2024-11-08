# coding: utf-8

"""
    Sensorbucket API

    SensorBucket processes data from different sources and devices into a single standardized format.  An applications connected to SensorBucket, can use all devices SensorBucket supports.  Missing a device or source? SensorBucket is designed to be scalable and extendable. Create your own worker that receives data from an AMQP source, process said data and output in the expected worker output format.  Find out more at: https://developer.sensorbucket.nl/  Developed and designed by Provincie Zeeland and Pollex' 

    The version of the OpenAPI document: 1.2.5
    Contact: info@pollex.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from sensorbucket.models.datastream import Datastream
from sensorbucket.models.device import Device
from sensorbucket.models.sensor import Sensor
from typing import Optional, Set
from typing_extensions import Self

class GetDatastream200ResponseData(BaseModel):
    """
    GetDatastream200ResponseData
    """ # noqa: E501
    datastream: Optional[Datastream] = None
    device: Optional[Device] = None
    sensor: Optional[Sensor] = None
    latest_measurement_value: Optional[Union[StrictFloat, StrictInt]] = None
    latest_measurement_timestamp: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["datastream", "device", "sensor", "latest_measurement_value", "latest_measurement_timestamp"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetDatastream200ResponseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of datastream
        if self.datastream:
            _dict['datastream'] = self.datastream.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sensor
        if self.sensor:
            _dict['sensor'] = self.sensor.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetDatastream200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "datastream": Datastream.from_dict(obj["datastream"]) if obj.get("datastream") is not None else None,
            "device": Device.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "sensor": Sensor.from_dict(obj["sensor"]) if obj.get("sensor") is not None else None,
            "latest_measurement_value": obj.get("latest_measurement_value"),
            "latest_measurement_timestamp": obj.get("latest_measurement_timestamp")
        })
        return _obj


