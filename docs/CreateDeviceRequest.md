# CreateDeviceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**description** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**location_description** | **str** |  | [optional] 
**properties** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.create_device_request import CreateDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeviceRequest from a JSON string
create_device_request_instance = CreateDeviceRequest.from_json(json)
# print the JSON string representation of the object
print CreateDeviceRequest.to_json()

# convert the object into a dict
create_device_request_dict = create_device_request_instance.to_dict()
# create an instance of CreateDeviceRequest from a dict
create_device_request_form_dict = create_device_request.from_dict(create_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


