# GetSensor200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**Sensor**](Sensor.md) |  | [optional] 

## Example

```python
from sensorbucket.models.get_sensor200_response import GetSensor200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSensor200Response from a JSON string
get_sensor200_response_instance = GetSensor200Response.from_json(json)
# print the JSON string representation of the object
print(GetSensor200Response.to_json())

# convert the object into a dict
get_sensor200_response_dict = get_sensor200_response_instance.to_dict()
# create an instance of GetSensor200Response from a dict
get_sensor200_response_from_dict = GetSensor200Response.from_dict(get_sensor200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


