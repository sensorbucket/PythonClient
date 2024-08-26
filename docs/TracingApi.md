# sensorbucket.TracingApi

All URIs are relative to *https://sensorbucket.nl/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_ingresses**](TracingApi.md#list_ingresses) | **GET** /ingresses | List ingresses
[**list_traces**](TracingApi.md#list_traces) | **GET** /tracing | List traces


# **list_ingresses**
> ListIngresses200Response list_ingresses(cursor=cursor, limit=limit)

List ingresses

Lists ingresses that match the provided filter. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.list_ingresses200_response import ListIngresses200Response
from sensorbucket.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sensorbucket.nl/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorbucket.Configuration(
    host = "https://sensorbucket.nl/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = sensorbucket.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: CookieSession
configuration.api_key['CookieSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieSession'] = 'Bearer'

# Enter a context with an instance of the API client
with sensorbucket.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorbucket.TracingApi(api_client)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # List ingresses
        api_response = api_instance.list_ingresses(cursor=cursor, limit=limit)
        print("The response of TracingApi->list_ingresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracingApi->list_ingresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**ListIngresses200Response**](ListIngresses200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched ingresses |  -  |
**400** | The request failed because of a malformed or invalid request |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_traces**
> ListTraces200Response list_traces(cursor=cursor, limit=limit, tracing_id=tracing_id, device_id=device_id, status=status, duration_greater_than=duration_greater_than, duration_smaller_than=duration_smaller_than)

List traces

Lists traces that match the provided filter. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.list_traces200_response import ListTraces200Response
from sensorbucket.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sensorbucket.nl/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sensorbucket.Configuration(
    host = "https://sensorbucket.nl/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = sensorbucket.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: CookieSession
configuration.api_key['CookieSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieSession'] = 'Bearer'

# Enter a context with an instance of the API client
with sensorbucket.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorbucket.TracingApi(api_client)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)
    tracing_id = ['tracing_id_example'] # List[str] |  (optional)
    device_id = 5 # int |  (optional)
    status = 2 # int |  (optional)
    duration_greater_than = 5 # int |  (optional)
    duration_smaller_than = 10 # int |  (optional)

    try:
        # List traces
        api_response = api_instance.list_traces(cursor=cursor, limit=limit, tracing_id=tracing_id, device_id=device_id, status=status, duration_greater_than=duration_greater_than, duration_smaller_than=duration_smaller_than)
        print("The response of TracingApi->list_traces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TracingApi->list_traces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 
 **tracing_id** | [**List[str]**](str.md)|  | [optional] 
 **device_id** | **int**|  | [optional] 
 **status** | **int**|  | [optional] 
 **duration_greater_than** | **int**|  | [optional] 
 **duration_smaller_than** | **int**|  | [optional] 

### Return type

[**ListTraces200Response**](ListTraces200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched traces |  -  |
**400** | The request failed because of a malformed or invalid request |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

