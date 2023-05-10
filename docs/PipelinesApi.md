# openapi_client.PipelinesApi

All URIs are relative to *https://sensorbucket.nl/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pipeline**](PipelinesApi.md#create_pipeline) | **POST** /pipelines | Create pipeline
[**disable_pipeline**](PipelinesApi.md#disable_pipeline) | **DELETE** /pipelines/{id} | Disable pipeline
[**get_pipeline**](PipelinesApi.md#get_pipeline) | **GET** /pipelines/{id} | Get pipeline
[**list_pipelines**](PipelinesApi.md#list_pipelines) | **GET** /pipelines | List pipelines
[**update_pipeline**](PipelinesApi.md#update_pipeline) | **PATCH** /pipelines/{id} | Update pipeline


# **create_pipeline**
> CreatePipeline200Response create_pipeline(create_pipeline_request=create_pipeline_request)

Create pipeline

Create a new pipeline.   A pipeline determines which workers, in which order the incoming data will be processed by.  A pipeline step is used as routing key in the Message Queue. This might be changed in future releases.  **Note:** currently there are no validations in place on whether a worker for the provided step actually exists. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.create_pipeline200_response import CreatePipeline200Response
from openapi_client.models.create_pipeline_request import CreatePipelineRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sensorbucket.nl/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sensorbucket.nl/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PipelinesApi(api_client)
    create_pipeline_request = openapi_client.CreatePipelineRequest() # CreatePipelineRequest |  (optional)

    try:
        # Create pipeline
        api_response = api_instance.create_pipeline(create_pipeline_request=create_pipeline_request)
        print("The response of PipelinesApi->create_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->create_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pipeline_request** | [**CreatePipelineRequest**](CreatePipelineRequest.md)|  | [optional] 

### Return type

[**CreatePipeline200Response**](CreatePipeline200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created pipeline |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_pipeline**
> DisablePipeline200Response disable_pipeline(id)

Disable pipeline

Disables a pipeline by setting its status to inactive.  Inactive pipelines will - by default - not appear in the `ListPipelines` and `GetPipeline` endpoints, unless the `status=inactive` query parameter is given on that endpoint. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.disable_pipeline200_response import DisablePipeline200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sensorbucket.nl/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sensorbucket.nl/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PipelinesApi(api_client)
    id = 'id_example' # str | The UUID of the pipeline

    try:
        # Disable pipeline
        api_response = api_instance.disable_pipeline(id)
        print("The response of PipelinesApi->disable_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->disable_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the pipeline | 

### Return type

[**DisablePipeline200Response**](DisablePipeline200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | pipeline disabled |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found or because the resource is disabled  |  -  |
**405** | The request failed because the request is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> GetPipeline200Response get_pipeline(id, status=status)

Get pipeline

Get the pipeline with the given identifier.  This endpoint by default returns a 404 Not Found for inactive pipelines. To get an inactive pipeline, provide the `status=inactive` query parameter. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.get_pipeline200_response import GetPipeline200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sensorbucket.nl/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sensorbucket.nl/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PipelinesApi(api_client)
    id = 'id_example' # str | The UUID of the pipeline
    status = ['[active, inactive]'] # List[str] | The status of the pipeline. Use `inactive` to view inactive pipelines instead of getting a 404 error  (optional)

    try:
        # Get pipeline
        api_response = api_instance.get_pipeline(id, status=status)
        print("The response of PipelinesApi->get_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the pipeline | 
 **status** | [**List[str]**](str.md)| The status of the pipeline. Use &#x60;inactive&#x60; to view inactive pipelines instead of getting a 404 error  | [optional] 

### Return type

[**GetPipeline200Response**](GetPipeline200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched pipeline |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found or because the resource is disabled  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipelines**
> ListPipelines200Response list_pipelines(inactive=inactive, step=step, cursor=cursor, limit=limit)

List pipelines

List pipelines. By default only `state=active` pipelines are returned. By providing the query parameter `inactive` only the inactive pipelines will be returned.  Pipelines can be filtered by providing one or more `step`s. This query parameter can be repeated to include more steps. When multiple steps are given, pipelines containing one of the given steps will be returned. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.list_pipelines200_response import ListPipelines200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sensorbucket.nl/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sensorbucket.nl/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PipelinesApi(api_client)
    inactive = True # bool | Only show inactive pipelines (optional)
    step = ['[thethingsnetwork, multiflexmeter]'] # List[str] | Only show pipelines that include at least one of these steps (optional)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 3.4 # float | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # List pipelines
        api_response = api_instance.list_pipelines(inactive=inactive, step=step, cursor=cursor, limit=limit)
        print("The response of PipelinesApi->list_pipelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->list_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inactive** | **bool**| Only show inactive pipelines | [optional] 
 **step** | [**List[str]**](str.md)| Only show pipelines that include at least one of these steps | [optional] 
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **float**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**ListPipelines200Response**](ListPipelines200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched pipelines |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline**
> UpdatePipeline200Response update_pipeline(id, update_pipeline_request=update_pipeline_request)

Update pipeline

Update some properties of the pipeline with the given identifier.   Setting an invalid state or making an invalid state transition will result in an error. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.update_pipeline200_response import UpdatePipeline200Response
from openapi_client.models.update_pipeline_request import UpdatePipelineRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sensorbucket.nl/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://sensorbucket.nl/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PipelinesApi(api_client)
    id = 'id_example' # str | The UUID of the pipeline
    update_pipeline_request = openapi_client.UpdatePipelineRequest() # UpdatePipelineRequest |  (optional)

    try:
        # Update pipeline
        api_response = api_instance.update_pipeline(id, update_pipeline_request=update_pipeline_request)
        print("The response of PipelinesApi->update_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->update_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the pipeline | 
 **update_pipeline_request** | [**UpdatePipelineRequest**](UpdatePipelineRequest.md)|  | [optional] 

### Return type

[**UpdatePipeline200Response**](UpdatePipeline200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated pipeline |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found or because the resource is disabled  |  -  |
**405** | The request failed because the request is invalid.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

