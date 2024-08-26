# SensorGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**sensors** | **List[int]** |  | 

## Example

```python
from sensorbucket.models.sensor_group import SensorGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SensorGroup from a JSON string
sensor_group_instance = SensorGroup.from_json(json)
# print the JSON string representation of the object
print(SensorGroup.to_json())

# convert the object into a dict
sensor_group_dict = sensor_group_instance.to_dict()
# create an instance of SensorGroup from a dict
sensor_group_from_dict = SensorGroup.from_dict(sensor_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


