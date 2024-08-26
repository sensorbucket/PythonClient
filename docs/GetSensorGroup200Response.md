# GetSensorGroup200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**SensorGroup**](SensorGroup.md) |  | [optional] 

## Example

```python
from sensorbucket.models.get_sensor_group200_response import GetSensorGroup200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSensorGroup200Response from a JSON string
get_sensor_group200_response_instance = GetSensorGroup200Response.from_json(json)
# print the JSON string representation of the object
print(GetSensorGroup200Response.to_json())

# convert the object into a dict
get_sensor_group200_response_dict = get_sensor_group200_response_instance.to_dict()
# create an instance of GetSensorGroup200Response from a dict
get_sensor_group200_response_from_dict = GetSensorGroup200Response.from_dict(get_sensor_group200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


