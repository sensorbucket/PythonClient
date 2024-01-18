# sensorbucket.UplinkApi

All URIs are relative to *https://sensorbucket.nl/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_uplink_data**](UplinkApi.md#process_uplink_data) | **POST** /uplinks/{pipeline_id} | Process uplink message


# **process_uplink_data**
> process_uplink_data(pipeline_id, body=body)

Process uplink message

Push an uplink message to the HTTP Importer for processing.  The request body and content-type can be anything the workers (defined by the pipeline steps) in the pipeline expect.  As this process is asynchronuous, any processing error will not be returned in the response. Only if the HTTP Importer is unable to push the message to the Message Queue, will an error be returned.  

### Example

* Basic Authentication (basicAuth):

```python
import sensorbucket
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

# Configure HTTP basic authorization: basicAuth
configuration = sensorbucket.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with sensorbucket.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensorbucket.UplinkApi(api_client)
    pipeline_id = 'c4d4fabd-9109-40cd-88b0-be40ca1745f7' # str | The UUID of the pipeline
    body = None # object |  (optional)

    try:
        # Process uplink message
        api_instance.process_uplink_data(pipeline_id, body=body)
    except Exception as e:
        print("Exception when calling UplinkApi->process_uplink_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**| The UUID of the pipeline | 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Accepted uplink |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found or is disabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

