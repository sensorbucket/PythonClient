# coding: utf-8

"""
    Sensorbucket API

    SensorBucket processes data from different sources and devices into a single standardized format.  An applications connected to SensorBucket, can use all devices SensorBucket supports.  Missing a device or source? SensorBucket is designed to be scalable and extendable. Create your own worker that receives data from an AMQP source, process said data and output in the expected worker output format.  Find out more at: https://developer.sensorbucket.nl/  Developed and designed by Provincie Zeeland and Pollex' 

    The version of the OpenAPI document: 1.2.0-rc1
    Contact: info@pollex.nl
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
import urllib
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
            'Noop', 
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


