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


from typing import Optional
from pydantic import BaseModel, StrictStr

class DisablePipeline200Response(BaseModel):
    """
    DisablePipeline200Response
    """
    message: Optional[StrictStr] = None
    __properties = ["message"]

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
    def from_json(cls, json_str: str) -> DisablePipeline200Response:
        """Create an instance of DisablePipeline200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DisablePipeline200Response:
        """Create an instance of DisablePipeline200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DisablePipeline200Response.parse_obj(obj)

        _obj = DisablePipeline200Response.parse_obj({
            "message": obj.get("message")
        })
        return _obj

