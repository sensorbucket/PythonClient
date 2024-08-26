# CreateSensorGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sensorbucket.models.create_sensor_group_request import CreateSensorGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSensorGroupRequest from a JSON string
create_sensor_group_request_instance = CreateSensorGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSensorGroupRequest.to_json())

# convert the object into a dict
create_sensor_group_request_dict = create_sensor_group_request_instance.to_dict()
# create an instance of CreateSensorGroupRequest from a dict
create_sensor_group_request_from_dict = CreateSensorGroupRequest.from_dict(create_sensor_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


