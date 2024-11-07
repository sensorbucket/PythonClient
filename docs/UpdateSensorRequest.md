# UpdateSensorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**properties** | **object** |  | [optional] 
**archive_time** | **int** |  | [optional] 

## Example

```python
from sensorbucket.models.update_sensor_request import UpdateSensorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSensorRequest from a JSON string
update_sensor_request_instance = UpdateSensorRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSensorRequest.to_json())

# convert the object into a dict
update_sensor_request_dict = update_sensor_request_instance.to_dict()
# create an instance of UpdateSensorRequest from a dict
update_sensor_request_from_dict = UpdateSensorRequest.from_dict(update_sensor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


