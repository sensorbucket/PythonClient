# sensorbucket.WorkersApi

All URIs are relative to *https://sensorbucket.nl/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worker**](WorkersApi.md#create_worker) | **POST** /workers | Create Worker
[**get_worker**](WorkersApi.md#get_worker) | **GET** /workers/{id} | Get worker
[**get_worker_user_code**](WorkersApi.md#get_worker_user_code) | **GET** /workers/{id}/usercode | Get the User Code for a Worker
[**list_workers**](WorkersApi.md#list_workers) | **GET** /workers | List workers
[**update_worker**](WorkersApi.md#update_worker) | **PATCH** /workers/{id} | Update worker properties


# **create_worker**
> CreateWorker201Response create_worker(create_user_worker_request=create_user_worker_request)

Create Worker

Create a new worker 

### Example

* Basic Authentication (basicAuth):

```python
import sensorbucket
from sensorbucket.models.create_user_worker_request import CreateUserWorkerRequest
from sensorbucket.models.create_worker201_response import CreateWorker201Response
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
    api_instance = sensorbucket.WorkersApi(api_client)
    create_user_worker_request = sensorbucket.CreateUserWorkerRequest() # CreateUserWorkerRequest |  (optional)

    try:
        # Create Worker
        api_response = api_instance.create_worker(create_user_worker_request=create_user_worker_request)
        print("The response of WorkersApi->create_worker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkersApi->create_worker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_worker_request** | [**CreateUserWorkerRequest**](CreateUserWorkerRequest.md)|  | [optional] 

### Return type

[**CreateWorker201Response**](CreateWorker201Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created worker |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worker**
> GetWorker200Response get_worker(id)

Get worker

Get the worker with the given identifier. 

### Example

* Basic Authentication (basicAuth):

```python
import sensorbucket
from sensorbucket.models.get_worker200_response import GetWorker200Response
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
    api_instance = sensorbucket.WorkersApi(api_client)
    id = 'id_example' # str | The UUID of the worker

    try:
        # Get worker
        api_response = api_instance.get_worker(id)
        print("The response of WorkersApi->get_worker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkersApi->get_worker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the worker | 

### Return type

[**GetWorker200Response**](GetWorker200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched worker |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worker_user_code**
> GetWorkerUserCode200Response get_worker_user_code(id)

Get the User Code for a Worker

Get the worker with the given identifier. 

### Example

* Basic Authentication (basicAuth):

```python
import sensorbucket
from sensorbucket.models.get_worker_user_code200_response import GetWorkerUserCode200Response
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
    api_instance = sensorbucket.WorkersApi(api_client)
    id = 'id_example' # str | The UUID of the worker

    try:
        # Get the User Code for a Worker
        api_response = api_instance.get_worker_user_code(id)
        print("The response of WorkersApi->get_worker_user_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkersApi->get_worker_user_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the worker | 

### Return type

[**GetWorkerUserCode200Response**](GetWorkerUserCode200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched worker user code |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workers**
> ListWorkers200Response list_workers(cursor=cursor, limit=limit, id=id)

List workers

Lists traces that match the provided filter. 

### Example

* Basic Authentication (basicAuth):

```python
import sensorbucket
from sensorbucket.models.list_workers200_response import ListWorkers200Response
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
    api_instance = sensorbucket.WorkersApi(api_client)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)
    id = ['id_example'] # List[str] | Filter by Pipeline IDs  (optional)

    try:
        # List workers
        api_response = api_instance.list_workers(cursor=cursor, limit=limit, id=id)
        print("The response of WorkersApi->list_workers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkersApi->list_workers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 
 **id** | [**List[str]**](str.md)| Filter by Pipeline IDs  | [optional] 

### Return type

[**ListWorkers200Response**](ListWorkers200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched workers |  -  |
**400** | The request failed because of a malformed or invalid request |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_worker**
> UpdateWorker200Response update_worker(id, update_worker_request=update_worker_request)

Update worker properties

Update a some properties of the worker with the given identifier.  The request body should contain one or more modifiable properties of the Worker. 

### Example

* Basic Authentication (basicAuth):

```python
import sensorbucket
from sensorbucket.models.update_worker200_response import UpdateWorker200Response
from sensorbucket.models.update_worker_request import UpdateWorkerRequest
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
    api_instance = sensorbucket.WorkersApi(api_client)
    id = 'id_example' # str | The UUID of the worker
    update_worker_request = sensorbucket.UpdateWorkerRequest() # UpdateWorkerRequest |  (optional)

    try:
        # Update worker properties
        api_response = api_instance.update_worker(id, update_worker_request=update_worker_request)
        print("The response of WorkersApi->update_worker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkersApi->update_worker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the worker | 
 **update_worker_request** | [**UpdateWorkerRequest**](UpdateWorkerRequest.md)|  | [optional] 

### Return type

[**UpdateWorker200Response**](UpdateWorker200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated worker properties |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

