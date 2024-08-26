# UpdateSensorGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sensorbucket.models.update_sensor_group_request import UpdateSensorGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSensorGroupRequest from a JSON string
update_sensor_group_request_instance = UpdateSensorGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSensorGroupRequest.to_json())

# convert the object into a dict
update_sensor_group_request_dict = update_sensor_group_request_instance.to_dict()
# create an instance of UpdateSensorGroupRequest from a dict
update_sensor_group_request_from_dict = UpdateSensorGroupRequest.from_dict(update_sensor_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


