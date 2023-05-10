# UpdateDeviceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **float** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**location_description** | **str** |  | [optional] 
**properties** | **object** |  | [optional] 

## Example

```python
from sensorbucket.models.update_device_request import UpdateDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeviceRequest from a JSON string
update_device_request_instance = UpdateDeviceRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDeviceRequest.to_json()

# convert the object into a dict
update_device_request_dict = update_device_request_instance.to_dict()
# create an instance of UpdateDeviceRequest from a dict
update_device_request_form_dict = update_device_request.from_dict(update_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


