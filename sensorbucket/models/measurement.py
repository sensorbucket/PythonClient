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
from typing import Optional, Set
from typing_extensions import Self

class Measurement(BaseModel):
    """
    Measurement
    """ # noqa: E501
    uplink_message_id: StrictStr
    device_id: StrictInt
    device_code: StrictStr
    device_description: Optional[StrictStr] = None
    device_latitude: Optional[Union[StrictFloat, StrictInt]] = None
    device_longitude: Optional[Union[StrictFloat, StrictInt]] = None
    device_altitude: Optional[Union[StrictFloat, StrictInt]] = None
    device_location_description: Optional[StrictStr] = None
    device_properties: Optional[Dict[str, Any]] = None
    device_state: StrictInt
    sensor_id: StrictInt
    sensor_code: StrictStr
    sensor_description: Optional[StrictStr] = None
    sensor_external_id: StrictStr
    sensor_properties: Optional[Dict[str, Any]] = None
    sensor_brand: Optional[StrictStr] = None
    sensor_archive_time: Optional[StrictInt] = None
    datastream_id: StrictStr
    datastream_description: Optional[StrictStr] = None
    datastream_observed_property: StrictStr
    datastream_unit_of_measurement: StrictStr
    measurement_timestamp: datetime
    measurement_value: Union[StrictFloat, StrictInt]
    measurement_latitude: Optional[Union[StrictFloat, StrictInt]] = None
    measurement_longitude: Optional[Union[StrictFloat, StrictInt]] = None
    measurement_altitude: Optional[Union[StrictFloat, StrictInt]] = None
    measurement_properties: Optional[Dict[str, Any]] = None
    measurement_expiration: datetime
    created_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["uplink_message_id", "device_id", "device_code", "device_description", "device_latitude", "device_longitude", "device_altitude", "device_location_description", "device_properties", "device_state", "sensor_id", "sensor_code", "sensor_description", "sensor_external_id", "sensor_properties", "sensor_brand", "sensor_archive_time", "datastream_id", "datastream_description", "datastream_observed_property", "datastream_unit_of_measurement", "measurement_timestamp", "measurement_value", "measurement_latitude", "measurement_longitude", "measurement_altitude", "measurement_properties", "measurement_expiration", "created_at"]

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
        """Create an instance of Measurement from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Measurement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uplink_message_id": obj.get("uplink_message_id"),
            "device_id": obj.get("device_id"),
            "device_code": obj.get("device_code"),
            "device_description": obj.get("device_description"),
            "device_latitude": obj.get("device_latitude"),
            "device_longitude": obj.get("device_longitude"),
            "device_altitude": obj.get("device_altitude"),
            "device_location_description": obj.get("device_location_description"),
            "device_properties": obj.get("device_properties"),
            "device_state": obj.get("device_state"),
            "sensor_id": obj.get("sensor_id"),
            "sensor_code": obj.get("sensor_code"),
            "sensor_description": obj.get("sensor_description"),
            "sensor_external_id": obj.get("sensor_external_id"),
            "sensor_properties": obj.get("sensor_properties"),
            "sensor_brand": obj.get("sensor_brand"),
            "sensor_archive_time": obj.get("sensor_archive_time"),
            "datastream_id": obj.get("datastream_id"),
            "datastream_description": obj.get("datastream_description"),
            "datastream_observed_property": obj.get("datastream_observed_property"),
            "datastream_unit_of_measurement": obj.get("datastream_unit_of_measurement"),
            "measurement_timestamp": obj.get("measurement_timestamp"),
            "measurement_value": obj.get("measurement_value"),
            "measurement_latitude": obj.get("measurement_latitude"),
            "measurement_longitude": obj.get("measurement_longitude"),
            "measurement_altitude": obj.get("measurement_altitude"),
            "measurement_properties": obj.get("measurement_properties"),
            "measurement_expiration": obj.get("measurement_expiration"),
            "created_at": obj.get("created_at")
        })
        return _obj


