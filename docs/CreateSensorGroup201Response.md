# CreateSensorGroup201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**SensorGroup**](SensorGroup.md) |  | [optional] 

## Example

```python
from sensorbucket.models.create_sensor_group201_response import CreateSensorGroup201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSensorGroup201Response from a JSON string
create_sensor_group201_response_instance = CreateSensorGroup201Response.from_json(json)
# print the JSON string representation of the object
print(CreateSensorGroup201Response.to_json())

# convert the object into a dict
create_sensor_group201_response_dict = create_sensor_group201_response_instance.to_dict()
# create an instance of CreateSensorGroup201Response from a dict
create_sensor_group201_response_from_dict = CreateSensorGroup201Response.from_dict(create_sensor_group201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


