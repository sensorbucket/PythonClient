# sensorbucket.TenantsApi

All URIs are relative to *https://sensorbucket.nl/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tenant_member**](TenantsApi.md#add_tenant_member) | **POST** /tenants/{tenant_id}/members | Add a User to a Tenant as member
[**list_tenants**](TenantsApi.md#list_tenants) | **GET** /tenants | Retrieves tenants
[**remove_tenant_member**](TenantsApi.md#remove_tenant_member) | **DELETE** /tenants/{tenant_id}/members/{user_id} | Removes a member from a tenant
[**update_tenant_member**](TenantsApi.md#update_tenant_member) | **PATCH** /tenants/{tenant_id}/members/{user_id} | Update a tenant member&#39;s permissions


# **add_tenant_member**
> AddTenantMember201Response add_tenant_member(tenant_id, add_tenant_member_request=add_tenant_member_request)

Add a User to a Tenant as member

Adds a user with the specific ID to the given Tenant as a member with the given permissions 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.add_tenant_member201_response import AddTenantMember201Response
from sensorbucket.models.add_tenant_member_request import AddTenantMemberRequest
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
    api_instance = sensorbucket.TenantsApi(api_client)
    tenant_id = 56 # int | The identifier of the tenant
    add_tenant_member_request = sensorbucket.AddTenantMemberRequest() # AddTenantMemberRequest |  (optional)

    try:
        # Add a User to a Tenant as member
        api_response = api_instance.add_tenant_member(tenant_id, add_tenant_member_request=add_tenant_member_request)
        print("The response of TenantsApi->add_tenant_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->add_tenant_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**| The identifier of the tenant | 
 **add_tenant_member_request** | [**AddTenantMemberRequest**](AddTenantMemberRequest.md)|  | [optional] 

### Return type

[**AddTenantMember201Response**](AddTenantMember201Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User added to Tenant |  -  |
**400** | The request failed because of a malformed or invalid request |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenants**
> ListTenants200Response list_tenants(name=name, state=state, is_member=is_member, cursor=cursor, limit=limit)

Retrieves tenants

Lists Tenants 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.list_tenants200_response import ListTenants200Response
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
    api_instance = sensorbucket.TenantsApi(api_client)
    name = 56 # int | Filter on specific name of a tenant (optional)
    state = 1 # int | Filter on soecific state of a tenant (optional)
    is_member = True # bool | Only show tenants that this user is a member of (optional)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # Retrieves tenants
        api_response = api_instance.list_tenants(name=name, state=state, is_member=is_member, cursor=cursor, limit=limit)
        print("The response of TenantsApi->list_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->list_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **int**| Filter on specific name of a tenant | [optional] 
 **state** | **int**| Filter on soecific state of a tenant | [optional] 
 **is_member** | **bool**| Only show tenants that this user is a member of | [optional] 
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**ListTenants200Response**](ListTenants200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched Tenants |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tenant_member**
> RemoveTenantMember200Response remove_tenant_member(tenant_id, user_id)

Removes a member from a tenant

Removes a member by the given user id from a tenant 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.remove_tenant_member200_response import RemoveTenantMember200Response
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
    api_instance = sensorbucket.TenantsApi(api_client)
    tenant_id = 56 # int | The identifier of the tenant
    user_id = 'user_id_example' # str | The identifier of the user

    try:
        # Removes a member from a tenant
        api_response = api_instance.remove_tenant_member(tenant_id, user_id)
        print("The response of TenantsApi->remove_tenant_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->remove_tenant_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**| The identifier of the tenant | 
 **user_id** | **str**| The identifier of the user | 

### Return type

[**RemoveTenantMember200Response**](RemoveTenantMember200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

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

# **update_tenant_member**
> RemoveTenantMember200Response update_tenant_member(tenant_id, user_id, update_tenant_member_request=update_tenant_member_request)

Update a tenant member's permissions

Update a tenant member's permissions 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.remove_tenant_member200_response import RemoveTenantMember200Response
from sensorbucket.models.update_tenant_member_request import UpdateTenantMemberRequest
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
    api_instance = sensorbucket.TenantsApi(api_client)
    tenant_id = 56 # int | The identifier of the tenant
    user_id = 'user_id_example' # str | The identifier of the user
    update_tenant_member_request = sensorbucket.UpdateTenantMemberRequest() # UpdateTenantMemberRequest |  (optional)

    try:
        # Update a tenant member's permissions
        api_response = api_instance.update_tenant_member(tenant_id, user_id, update_tenant_member_request=update_tenant_member_request)
        print("The response of TenantsApi->update_tenant_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **int**| The identifier of the tenant | 
 **user_id** | **str**| The identifier of the user | 
 **update_tenant_member_request** | [**UpdateTenantMemberRequest**](UpdateTenantMemberRequest.md)|  | [optional] 

### Return type

[**RemoveTenantMember200Response**](RemoveTenantMember200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: application/json
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

