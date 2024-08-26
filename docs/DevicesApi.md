# sensorbucket.DevicesApi

All URIs are relative to *https://sensorbucket.nl/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sensor_to_sensor_group**](DevicesApi.md#add_sensor_to_sensor_group) | **POST** /sensor-groups/{id}/sensors | Add sensor to a sensor group
[**create_device**](DevicesApi.md#create_device) | **POST** /devices | Create device
[**create_device_sensor**](DevicesApi.md#create_device_sensor) | **POST** /devices/{device_id}/sensors | Create sensor for device
[**create_sensor_group**](DevicesApi.md#create_sensor_group) | **POST** /sensor-groups | Create sensor group
[**delete_device_sensor**](DevicesApi.md#delete_device_sensor) | **DELETE** /device/{device_id}/sensors/{sensor_code} | Delete sensor
[**delete_sensor_from_sensor_group**](DevicesApi.md#delete_sensor_from_sensor_group) | **DELETE** /sensor-groups/{id}/sensors/{sensor_id} | Delete sensor from sensor group
[**delete_sensor_group**](DevicesApi.md#delete_sensor_group) | **DELETE** /sensor-groups/{id} | Delete sensor group
[**get_device**](DevicesApi.md#get_device) | **GET** /devices/{id} | Get device
[**get_sensor_group**](DevicesApi.md#get_sensor_group) | **GET** /sensor-groups/{id} | Get sensor group
[**list_device_sensors**](DevicesApi.md#list_device_sensors) | **GET** /devices/{device_id}/sensors | List sensors device
[**list_devices**](DevicesApi.md#list_devices) | **GET** /devices | List devices
[**list_sensor_groups**](DevicesApi.md#list_sensor_groups) | **GET** /sensor-groups | List sensor groups
[**list_sensors**](DevicesApi.md#list_sensors) | **GET** /sensors | List sensors
[**update_device**](DevicesApi.md#update_device) | **PATCH** /devices/{id} | Update device properties
[**update_sensor_group**](DevicesApi.md#update_sensor_group) | **PATCH** /sensor-groups/{id} | Update sensor group


# **add_sensor_to_sensor_group**
> AddSensorToSensorGroup201Response add_sensor_to_sensor_group(id, add_sensor_to_sensor_group_request=add_sensor_to_sensor_group_request)

Add sensor to a sensor group

Add a sensor by its ID to a sensor group by its ID 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.add_sensor_to_sensor_group201_response import AddSensorToSensorGroup201Response
from sensorbucket.models.add_sensor_to_sensor_group_request import AddSensorToSensorGroupRequest
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
    api_instance = sensorbucket.DevicesApi(api_client)
    id = 56 # int | The identifier of the Sensor Group
    add_sensor_to_sensor_group_request = sensorbucket.AddSensorToSensorGroupRequest() # AddSensorToSensorGroupRequest |  (optional)

    try:
        # Add sensor to a sensor group
        api_response = api_instance.add_sensor_to_sensor_group(id, add_sensor_to_sensor_group_request=add_sensor_to_sensor_group_request)
        print("The response of DevicesApi->add_sensor_to_sensor_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->add_sensor_to_sensor_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the Sensor Group | 
 **add_sensor_to_sensor_group_request** | [**AddSensorToSensorGroupRequest**](AddSensorToSensorGroupRequest.md)|  | [optional] 

### Return type

[**AddSensorToSensorGroup201Response**](AddSensorToSensorGroup201Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added sensor to sensor group |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device**
> CreateDevice201Response create_device(create_device_request=create_device_request)

Create device

Create a new device.  Depending on the type of device and the network it is registered on. The device might need specific properties to be set.   **For example:** A LoRaWAN device often requires a `dev_eui` property to be set. The system will match incoming traffic against that property. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.create_device201_response import CreateDevice201Response
from sensorbucket.models.create_device_request import CreateDeviceRequest
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
    api_instance = sensorbucket.DevicesApi(api_client)
    create_device_request = sensorbucket.CreateDeviceRequest() # CreateDeviceRequest |  (optional)

    try:
        # Create device
        api_response = api_instance.create_device(create_device_request=create_device_request)
        print("The response of DevicesApi->create_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_device_request** | [**CreateDeviceRequest**](CreateDeviceRequest.md)|  | [optional] 

### Return type

[**CreateDevice201Response**](CreateDevice201Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_sensor**
> CreateDeviceSensor201Response create_device_sensor(device_id, create_sensor_request=create_sensor_request)

Create sensor for device

Create a new sensor for the device with the given identifier.  A device can not have sensors with either a duplicate `code` or duplicate `external_id` field. As this would result in conflicts while matching incoming messages to devices and sensors. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.create_device_sensor201_response import CreateDeviceSensor201Response
from sensorbucket.models.create_sensor_request import CreateSensorRequest
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
    api_instance = sensorbucket.DevicesApi(api_client)
    device_id = 56 # int | The identifier of the device
    create_sensor_request = sensorbucket.CreateSensorRequest() # CreateSensorRequest |  (optional)

    try:
        # Create sensor for device
        api_response = api_instance.create_device_sensor(device_id, create_sensor_request=create_sensor_request)
        print("The response of DevicesApi->create_device_sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_device_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The identifier of the device | 
 **create_sensor_request** | [**CreateSensorRequest**](CreateSensorRequest.md)|  | [optional] 

### Return type

[**CreateDeviceSensor201Response**](CreateDeviceSensor201Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created new sensor for device |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sensor_group**
> CreateSensorGroup201Response create_sensor_group(create_sensor_group_request=create_sensor_group_request)

Create sensor group

Create a new sensor group. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.create_sensor_group201_response import CreateSensorGroup201Response
from sensorbucket.models.create_sensor_group_request import CreateSensorGroupRequest
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
    api_instance = sensorbucket.DevicesApi(api_client)
    create_sensor_group_request = sensorbucket.CreateSensorGroupRequest() # CreateSensorGroupRequest |  (optional)

    try:
        # Create sensor group
        api_response = api_instance.create_sensor_group(create_sensor_group_request=create_sensor_group_request)
        print("The response of DevicesApi->create_sensor_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->create_sensor_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sensor_group_request** | [**CreateSensorGroupRequest**](CreateSensorGroupRequest.md)|  | [optional] 

### Return type

[**CreateSensorGroup201Response**](CreateSensorGroup201Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_sensor**
> DeleteDeviceSensor200Response delete_device_sensor(device_id, sensor_code)

Delete sensor

Delete a sensor from the system.   Since a sensor can only be related to one and only one device at a time, the sensor will be deleted from the system completely 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.delete_device_sensor200_response import DeleteDeviceSensor200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    device_id = 56 # int | The identifier of the device
    sensor_code = 'sensor_code_example' # str | The code of the sensor

    try:
        # Delete sensor
        api_response = api_instance.delete_device_sensor(device_id, sensor_code)
        print("The response of DevicesApi->delete_device_sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_device_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The identifier of the device | 
 **sensor_code** | **str**| The code of the sensor | 

### Return type

[**DeleteDeviceSensor200Response**](DeleteDeviceSensor200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted sensor from device |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sensor_from_sensor_group**
> DeleteSensorFromSensorGroup200Response delete_sensor_from_sensor_group(id, sensor_id)

Delete sensor from sensor group

Delete a sensor from a sensor group 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.delete_sensor_from_sensor_group200_response import DeleteSensorFromSensorGroup200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    id = 56 # int | The identifier of the sensor group
    sensor_id = 56 # int | The id of the sensor

    try:
        # Delete sensor from sensor group
        api_response = api_instance.delete_sensor_from_sensor_group(id, sensor_id)
        print("The response of DevicesApi->delete_sensor_from_sensor_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_sensor_from_sensor_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the sensor group | 
 **sensor_id** | **int**| The id of the sensor | 

### Return type

[**DeleteSensorFromSensorGroup200Response**](DeleteSensorFromSensorGroup200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted sensor from sensor group |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sensor_group**
> DeleteSensorGroup200Response delete_sensor_group(id)

Delete sensor group

Delete a sensor group 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.delete_sensor_group200_response import DeleteSensorGroup200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    id = 56 # int | The id of the sensor group

    try:
        # Delete sensor group
        api_response = api_instance.delete_sensor_group(id)
        print("The response of DevicesApi->delete_sensor_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_sensor_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the sensor group | 

### Return type

[**DeleteSensorGroup200Response**](DeleteSensorGroup200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sensor group deleted |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> GetDevice200Response get_device(id)

Get device

Get the device with the given identifier.  The returned device will also include the full model of the sensors attached to that device. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.get_device200_response import GetDevice200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    id = 56 # int | The numeric ID of the device

    try:
        # Get device
        api_response = api_instance.get_device(id)
        print("The response of DevicesApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the device | 

### Return type

[**GetDevice200Response**](GetDevice200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched device |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensor_group**
> GetSensorGroup200Response get_sensor_group(id)

Get sensor group

Get the sensor group with the given identifier. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.get_sensor_group200_response import GetSensorGroup200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    id = 56 # int | The numeric ID of the sensor group

    try:
        # Get sensor group
        api_response = api_instance.get_sensor_group(id)
        print("The response of DevicesApi->get_sensor_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_sensor_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the sensor group | 

### Return type

[**GetSensorGroup200Response**](GetSensorGroup200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched sensor group |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_device_sensors**
> ListDeviceSensors200Response list_device_sensors(device_id, cursor=cursor, limit=limit)

List sensors device

List all sensors related to the device with the provided identifier 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.list_device_sensors200_response import ListDeviceSensors200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    device_id = 56 # int | The identifier of the device
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # List sensors device
        api_response = api_instance.list_device_sensors(device_id, cursor=cursor, limit=limit)
        print("The response of DevicesApi->list_device_sensors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_device_sensors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The identifier of the device | 
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**ListDeviceSensors200Response**](ListDeviceSensors200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Listed device sensors |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> ListDevices200Response list_devices(properties=properties, north=north, west=west, east=east, south=south, latitude=latitude, longitude=longitude, distance=distance, cursor=cursor, limit=limit, id=id, sensor_group=sensor_group)

List devices

Fetch a list of devices.  Devices can be filtered on three items: properties, distance from a location or a bounding box.  - Filtering on properties filters devices on whether their property attribute is a superset of the given JSON object value  - Distance from location filtering requires a latitude, longitude and distance (in meters). All devices within that range will be returned  - Bounding box requires a North,East,South and West point. All devices within that box will be returned.  The filters distance from location and bounding box are mutually exclusive. The location distance filter will take precedence. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.list_devices200_response import ListDevices200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    properties = '{ \"eui\": \"1122334455667788\" }' # str | Used to filter devices by its properties. This filters devices on whether their property contains the provided value. The value must be a JSON string and depending on your client should be URL Escaped (optional)
    north = 3.6175560329103202 # float | Used to filter devices within a bounding box (optional)
    west = 51.518796779610035 # float | Used to filter devices within a bounding box (optional)
    east = 51.47912508218688 # float | Used to filter devices within a bounding box (optional)
    south = 3.655955445579366 # float | Used to filter devices within a bounding box (optional)
    latitude = 51.496227862014685 # float | Used to filter devices within a distance from a point (optional)
    longitude = 3.615071953647924 # float | Used to filter devices within a distance from a point (optional)
    distance = 1000 # int | Used to filter devices within a distance from a point.  The distance is given in meters.  (optional)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)
    id = [56] # List[int] | Filter by Device IDs  (optional)
    sensor_group = [56] # List[int] | Filter by device group  (optional)

    try:
        # List devices
        api_response = api_instance.list_devices(properties=properties, north=north, west=west, east=east, south=south, latitude=latitude, longitude=longitude, distance=distance, cursor=cursor, limit=limit, id=id, sensor_group=sensor_group)
        print("The response of DevicesApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **properties** | **str**| Used to filter devices by its properties. This filters devices on whether their property contains the provided value. The value must be a JSON string and depending on your client should be URL Escaped | [optional] 
 **north** | **float**| Used to filter devices within a bounding box | [optional] 
 **west** | **float**| Used to filter devices within a bounding box | [optional] 
 **east** | **float**| Used to filter devices within a bounding box | [optional] 
 **south** | **float**| Used to filter devices within a bounding box | [optional] 
 **latitude** | **float**| Used to filter devices within a distance from a point | [optional] 
 **longitude** | **float**| Used to filter devices within a distance from a point | [optional] 
 **distance** | **int**| Used to filter devices within a distance from a point.  The distance is given in meters.  | [optional] 
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 
 **id** | [**List[int]**](int.md)| Filter by Device IDs  | [optional] 
 **sensor_group** | [**List[int]**](int.md)| Filter by device group  | [optional] 

### Return type

[**ListDevices200Response**](ListDevices200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sensor_groups**
> ListSensorGroups200Response list_sensor_groups(cursor=cursor, limit=limit)

List sensor groups

Fetch a list of sensor groups. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.list_sensor_groups200_response import ListSensorGroups200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # List sensor groups
        api_response = api_instance.list_sensor_groups(cursor=cursor, limit=limit)
        print("The response of DevicesApi->list_sensor_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_sensor_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**ListSensorGroups200Response**](ListSensorGroups200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sensors**
> ListDeviceSensors200Response list_sensors(cursor=cursor, limit=limit)

List sensors

List all sensors. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.list_device_sensors200_response import ListDeviceSensors200Response
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
    api_instance = sensorbucket.DevicesApi(api_client)
    cursor = 'cursor_example' # str | The cursor for the current page (optional)
    limit = 56 # int | The maximum amount of items per page. Not applicable if `cursor` parameter is given. System limits are in place.  (optional)

    try:
        # List sensors
        api_response = api_instance.list_sensors(cursor=cursor, limit=limit)
        print("The response of DevicesApi->list_sensors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_sensors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor for the current page | [optional] 
 **limit** | **int**| The maximum amount of items per page. Not applicable if &#x60;cursor&#x60; parameter is given. System limits are in place.  | [optional] 

### Return type

[**ListDeviceSensors200Response**](ListDeviceSensors200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetched sensors |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> UpdateDevice200Response update_device(id, update_device_request=update_device_request)

Update device properties

Update a some properties of the device with the given identifier.  The request body should contain one or more modifiable properties of the Device. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.update_device200_response import UpdateDevice200Response
from sensorbucket.models.update_device_request import UpdateDeviceRequest
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
    api_instance = sensorbucket.DevicesApi(api_client)
    id = 56 # int | The numeric ID of the device
    update_device_request = sensorbucket.UpdateDeviceRequest() # UpdateDeviceRequest |  (optional)

    try:
        # Update device properties
        api_response = api_instance.update_device(id, update_device_request=update_device_request)
        print("The response of DevicesApi->update_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->update_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the device | 
 **update_device_request** | [**UpdateDeviceRequest**](UpdateDeviceRequest.md)|  | [optional] 

### Return type

[**UpdateDevice200Response**](UpdateDevice200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated device properties |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sensor_group**
> UpdateSensorGroup200Response update_sensor_group(id, update_sensor_group_request=update_sensor_group_request)

Update sensor group

Update a some properties of the sensor group with the given identifier.  The request body should contain one or more modifiable properties of the sensor group. 

### Example

* Bearer Authentication (APIKey):
* Api Key Authentication (CookieSession):

```python
import sensorbucket
from sensorbucket.models.update_sensor_group200_response import UpdateSensorGroup200Response
from sensorbucket.models.update_sensor_group_request import UpdateSensorGroupRequest
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
    api_instance = sensorbucket.DevicesApi(api_client)
    id = 56 # int | The numeric ID of the sensor group
    update_sensor_group_request = sensorbucket.UpdateSensorGroupRequest() # UpdateSensorGroupRequest |  (optional)

    try:
        # Update sensor group
        api_response = api_instance.update_sensor_group(id, update_sensor_group_request=update_sensor_group_request)
        print("The response of DevicesApi->update_sensor_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->update_sensor_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the sensor group | 
 **update_sensor_group_request** | [**UpdateSensorGroupRequest**](UpdateSensorGroupRequest.md)|  | [optional] 

### Return type

[**UpdateSensorGroup200Response**](UpdateSensorGroup200Response.md)

### Authorization

[APIKey](../README.md#APIKey), [CookieSession](../README.md#CookieSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Sensor Group properties |  -  |
**401** | The request failed because the provided credentials are invalid or missing |  -  |
**403** | The request failed because the provided credentials do not have the required permissions to perform this action |  -  |
**404** | The request failed because the requested resource could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

