# sensorbucket.MeasurementsApi

All URIs are relative to *https://sensorbucket.nl/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_datastream**](MeasurementsApi.md#get_datastream) | **GET** /datastreams/{id} | Get datastream
[**list_datastreams**](MeasurementsApi.md#list_datastreams) | **GET** /datastreams | List all datastreams
[**query_measurements**](MeasurementsApi.md#query_measurements) | **GET** /measurements | Query measurements


# **get_datastream**
> GetDatastream200Response get_datastream(id)

Get datastream

Get the datastream with the given identifier.  The returned datastream will also include the full model of the sensors attached to that datastream. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.get_datastream200_response import GetDatastream200Response
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
    api_instance = sensorbucket.MeasurementsApi(api_client)
    id = 'id_example' # str | The UUID of the datastream

    try:
        # Get datastream
        api_response = api_instance.get_datastream(id)
        print("The response of MeasurementsApi->get_datastream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsApi->get_datastream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the datastream | 

### Return type

[**GetDatastream200Response**](GetDatastream200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched datastream |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datastreams**
> ListDatastreams200Response list_datastreams(sensor=sensor, cursor=cursor, limit=limit)

List all datastreams

List all datastreams.  A sensor can produce one or more timeseries of measurements. Such a unique timeserie is called a datastream.    **For example:** A Particulate Matter sensor might return count the number of particles smaller than 2.5 μg/cm2, 5 μg/cm2 and 10 μg/cm2. this is one sensor producing three datastreams.  Another example would be a worker which processes raw incoming values into meaningful data. An underwater pressure sensor might supply its measurement in milli Amperes, but the worker converts it to watercolumn in meters. The sensor now has two datastreams. Presusre in millivolt and watercolumn in meters. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.list_datastreams200_response import ListDatastreams200Response
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
    api_instance = sensorbucket.MeasurementsApi(api_client)
    sensor = [56] # List[int] | only return datastreams that are produced by the given sensor identifier (optional)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # List all datastreams
        api_response = api_instance.list_datastreams(sensor=sensor, cursor=cursor, limit=limit)
        print("The response of MeasurementsApi->list_datastreams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsApi->list_datastreams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor** | [**List[int]**](int.md)| only return datastreams that are produced by the given sensor identifier | [optional] 
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**ListDatastreams200Response**](ListDatastreams200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched datastreams |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_measurements**
> QueryMeasurements200Response query_measurements(start, end, device_id=device_id, datastream=datastream, sensor_code=sensor_code, cursor=cursor, limit=limit)

Query measurements

Query a list of measurements.  This endpoint is used to get all measurements that correspond with the given filters.  It is commonly required to get a single stream of measurements from a single sensor. This can be accomplished by  finding the corresponding datastream ID and using that in the `datastream` filter.   Most query parameters can be repeated to get an OR combination of filters. For example, providing the `datastream`  parameter twice will return measurements for either datastreams. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.query_measurements200_response import QueryMeasurements200Response
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
    api_instance = sensorbucket.MeasurementsApi(api_client)
    start = '2022-01-01T00:00Z' # datetime | 
    end = '2022-12-31T23:59:59Z' # datetime | 
    device_id = 'device_id_example' # str |  (optional)
    datastream = 'datastream_example' # str |  (optional)
    sensor_code = 'sensor_code_example' # str |  (optional)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # Query measurements
        api_response = api_instance.query_measurements(start, end, device_id=device_id, datastream=datastream, sensor_code=sensor_code, cursor=cursor, limit=limit)
        print("The response of MeasurementsApi->query_measurements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasurementsApi->query_measurements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 
 **device_id** | **str**|  | [optional] 
 **datastream** | **str**|  | [optional] 
 **sensor_code** | **str**|  | [optional] 
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**QueryMeasurements200Response**](QueryMeasurements200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched measurements |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

