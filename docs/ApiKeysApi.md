# sensorbucket.ApiKeysApi

All URIs are relative to *https://sensorbucket.nl/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeysApi.md#create_api_key) | **POST** /api-keys | Creates a new API key for the given Tenant
[**list_api_keys**](ApiKeysApi.md#list_api_keys) | **GET** /api-keys/list | List API Keys
[**revoke_api_key**](ApiKeysApi.md#revoke_api_key) | **DELETE** /api-keys/{api_key_id} | Revokes an API key


# **create_api_key**
> ApiKeyCreated create_api_key(create_api_key_request=create_api_key_request)

Creates a new API key for the given Tenant

Create an API key for a tenant with an expiration date. Permissions for the API key within that organisation must be set 

### Example

* Basic Authentication (basicAuth):

```python
import sensorbucket
from sensorbucket.models.api_key_created import ApiKeyCreated
from sensorbucket.models.create_api_key_request import CreateApiKeyRequest
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
    api_instance = sensorbucket.ApiKeysApi(api_client)
    create_api_key_request = sensorbucket.CreateApiKeyRequest() # CreateApiKeyRequest |  (optional)

    try:
        # Creates a new API key for the given Tenant
        api_response = api_instance.create_api_key(create_api_key_request=create_api_key_request)
        print("The response of ApiKeysApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)|  | [optional] 

### Return type

[**ApiKeyCreated**](ApiKeyCreated.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created API key |  -  |
**400** | The request failed because of a malformed or invalid request |  -  |
**500** | The request failed because of an unexpected server error |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ListApiKeys200Response list_api_keys(tenant_id=tenant_id, cursor=cursor, limit=limit)

List API Keys

Lists API Keys 

### Example

* Basic Authentication (basicAuth):

```python
import sensorbucket
from sensorbucket.models.list_api_keys200_response import ListApiKeys200Response
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
    api_instance = sensorbucket.ApiKeysApi(api_client)
    tenant_id = 56 # int | The id of the tenant from which to retrieve API keys (optional)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # List API Keys
        api_response = api_instance.list_api_keys(tenant_id=tenant_id, cursor=cursor, limit=limit)
        print("The response of ApiKeysApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->list_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**| The id of the tenant from which to retrieve API keys | [optional] 
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**ListApiKeys200Response**](ListApiKeys200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched API keys |  -  |
**400** | The request failed because of a malformed or invalid request |  -  |
**500** | The request failed because of an unexpected server error |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_key**
> revoke_api_key(api_key_id)

Revokes an API key

Revokes an API key so that it can't be used anymore 

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
    api_instance = sensorbucket.ApiKeysApi(api_client)
    api_key_id = 56 # int | The identifier of the API key

    try:
        # Revokes an API key
        api_instance.revoke_api_key(api_key_id)
    except Exception as e:
        print("Exception when calling ApiKeysApi->revoke_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**| The identifier of the API key | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | The request failed because of a malformed or invalid request |  -  |
**500** | The request failed because of an unexpected server error |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

