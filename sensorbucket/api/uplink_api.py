# coding: utf-8

"""
    Sensorbucket API

    SensorBucket processes data from different sources and devices into a single standardized format.  An applications connected to SensorBucket, can use all devices SensorBucket supports.  Missing a device or source? SensorBucket is designed to be scalable and extendable. Create your own worker that receives data from an AMQP source, process said data and output in the expected worker output format.  Find out more at: https://developer.sensorbucket.nl/  Developed and designed by Provincie Zeeland and Pollex' 

    The version of the OpenAPI document: 1.2.4
    Contact: info@pollex.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
import urllib
from datetime import (
    datetime,
    date,
    timedelta,
)
import time
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Generator, Dict, List, Optional, Tuple, Union 
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated

from sensorbucket.api_client import ApiClient, RequestSerialized
from sensorbucket.api_response import ApiResponse
from sensorbucket.rest import RESTResponseType


class UplinkApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def process_uplink_data(
        self,
        pipeline_id: Annotated[StrictStr, Field(description="The UUID of the pipeline")],
        body: Optional[Dict[str, Any]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Process uplink message

        Push an uplink message to the HTTP Importer for processing.  The request body and content-type can be anything the workers (defined by the pipeline steps) in the pipeline expect.  As this process is asynchronuous, any processing error will not be returned in the response. Only if the HTTP Importer is unable to push the message to the Message Queue, will an error be returned.  

        :param pipeline_id: The UUID of the pipeline (required)
        :type pipeline_id: str
        :param body:
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._process_uplink_data_serialize(
            pipeline_id=pipeline_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '401': None,
            '403': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def process_uplink_data_with_http_info(
        self,
        pipeline_id: Annotated[StrictStr, Field(description="The UUID of the pipeline")],
        body: Optional[Dict[str, Any]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Process uplink message

        Push an uplink message to the HTTP Importer for processing.  The request body and content-type can be anything the workers (defined by the pipeline steps) in the pipeline expect.  As this process is asynchronuous, any processing error will not be returned in the response. Only if the HTTP Importer is unable to push the message to the Message Queue, will an error be returned.  

        :param pipeline_id: The UUID of the pipeline (required)
        :type pipeline_id: str
        :param body:
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._process_uplink_data_serialize(
            pipeline_id=pipeline_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '401': None,
            '403': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def process_uplink_data_without_preload_content(
        self,
        pipeline_id: Annotated[StrictStr, Field(description="The UUID of the pipeline")],
        body: Optional[Dict[str, Any]] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Process uplink message

        Push an uplink message to the HTTP Importer for processing.  The request body and content-type can be anything the workers (defined by the pipeline steps) in the pipeline expect.  As this process is asynchronuous, any processing error will not be returned in the response. Only if the HTTP Importer is unable to push the message to the Message Queue, will an error be returned.  

        :param pipeline_id: The UUID of the pipeline (required)
        :type pipeline_id: str
        :param body:
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._process_uplink_data_serialize(
            pipeline_id=pipeline_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '401': None,
            '403': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _process_uplink_data_serialize(
        self,
        pipeline_id,
        body,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if pipeline_id is not None:
            _path_params['pipeline_id'] = pipeline_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            _body_params = body



        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'APIKey', 
            'CookieSession'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/uplinks/{pipeline_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )





def _timezone(utc_offset):
    '''
    Return a string representing the timezone offset.

    >>> _timezone(0)
    '+00:00'
    >>> _timezone(3600)
    '+01:00'
    >>> _timezone(-28800)
    '-08:00'
    >>> _timezone(-8 * 60 * 60)
    '-08:00'
    >>> _timezone(-30 * 60)
    '-00:30'
    '''
    # Python's division uses floor(), not round() like in other languages:
    #   -1 / 2 == -1 and not -1 / 2 == 0
    # That's why we use abs(utc_offset).
    hours = abs(utc_offset) // 3600
    minutes = abs(utc_offset) % 3600 // 60
    sign = (utc_offset < 0 and '-') or '+'
    return '%c%02d:%02d' % (sign, hours, minutes)

def _timedelta_to_seconds(td):
    '''
    >>> _timedelta_to_seconds(timedelta(hours=3))
    10800
    >>> _timedelta_to_seconds(timedelta(hours=3, minutes=15))
    11700
    >>> _timedelta_to_seconds(timedelta(hours=-8))
    -28800
    '''
    return int((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6)

def _utc_offset(timestamp, use_system_timezone):
    '''
    Return the UTC offset of `timestamp`. If `timestamp` does not have any `tzinfo`, use
    the timezone informations stored locally on the system.

    >>> if time.localtime().tm_isdst:
    ...     system_timezone = -time.altzone
    ... else:
    ...     system_timezone = -time.timezone
    >>> _utc_offset(datetime.now(), True) == system_timezone
    True
    >>> _utc_offset(datetime.now(), False)
    0
    '''
    if (isinstance(timestamp, datetime) and
            timestamp.tzinfo is not None):
        return _timedelta_to_seconds(timestamp.utcoffset())
    elif use_system_timezone:
        if timestamp.year < 1970:
            # We use 1972 because 1970 doesn't have a leap day (feb 29)
            t = time.mktime(timestamp.replace(year=1972).timetuple())
        else:
            t = time.mktime(timestamp.timetuple())
        if time.localtime(t).tm_isdst: # pragma: no cover
            return -time.altzone
        else:
            return -time.timezone
    else:
        return 0

def _string(d, timezone):
    return ('%04d-%02d-%02dT%02d:%02d:%02d%s' %
            (d.year, d.month, d.day, d.hour, d.minute, d.second, timezone))

def _string_milliseconds(d, timezone):
    return ('%04d-%02d-%02dT%02d:%02d:%02d.%03d%s' %
            (d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond / 1000, timezone))

def _string_microseconds(d, timezone):
    return ('%04d-%02d-%02dT%02d:%02d:%02d.%06d%s' %
            (d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, timezone))

def _format(timestamp, string_format, utc, use_system_timezone):
    # Try to convert timestamp to datetime
    try:
        if use_system_timezone:
            timestamp = datetime.fromtimestamp(timestamp)
        else:
            timestamp = datetime.utcfromtimestamp(timestamp)
    except TypeError:
        pass

    if not isinstance(timestamp, date):
        raise TypeError('Expected timestamp or date object. Got %r.' %
                        type(timestamp))

    if not isinstance(timestamp, datetime):
        timestamp = datetime(*timestamp.timetuple()[:3])
    utc_offset = _utc_offset(timestamp, use_system_timezone)
    if utc:
        # local time -> utc
        return string_format(timestamp - timedelta(seconds=utc_offset), 'Z')
    else:
        return string_format(timestamp , _timezone(utc_offset))

def rfc3339format(timestamp, utc=False, use_system_timezone=True):
    '''
    Return a string formatted according to the :RFC:`3339`. If called with
    `utc=True`, it normalizes `timestamp` to the UTC date. If `timestamp` does
    not have any timezone information, uses the local timezone::

        >>> d = datetime(2008, 4, 2, 20)
        >>> rfc3339(d, utc=True, use_system_timezone=False)
        '2008-04-02T20:00:00Z'
        >>> rfc3339(d) # doctest: +ELLIPSIS
        '2008-04-02T20:00:00...'

    If called with `use_system_timezone=False` don't use the local timezone if
    `timestamp` does not have timezone informations and consider the offset to UTC
    to be zero::

        >>> rfc3339(d, use_system_timezone=False)
        '2008-04-02T20:00:00+00:00'

    `timestamp` must be a `datetime`, `date` or a timestamp as
    returned by `time.time()`::

        >>> rfc3339(0, utc=True, use_system_timezone=False)
        '1970-01-01T00:00:00Z'
        >>> rfc3339(date(2008, 9, 6), utc=True,
        ...         use_system_timezone=False)
        '2008-09-06T00:00:00Z'
        >>> rfc3339(date(2008, 9, 6),
        ...         use_system_timezone=False)
        '2008-09-06T00:00:00+00:00'
        >>> rfc3339('foo bar') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: Expected timestamp or date object. Got <... 'str'>.

    For dates before January 1st 1970, the timezones will be the ones used in
    1970. It might not be accurate, but on most sytem there is no timezone
    information before 1970.
    '''
    return _format(timestamp, _string, utc, use_system_timezone)
