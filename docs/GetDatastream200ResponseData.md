# GetDatastream200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastream** | [**Datastream**](Datastream.md) |  | [optional] 
**device** | [**Device**](Device.md) |  | [optional] 
**sensor** | [**Sensor**](Sensor.md) |  | [optional] 
**latest_measurement_value** | **float** |  | [optional] 
**latest_measurement_timestamp** | **datetime** |  | [optional] 

## Example

```python
from sensorbucket.models.get_datastream200_response_data import GetDatastream200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatastream200ResponseData from a JSON string
get_datastream200_response_data_instance = GetDatastream200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetDatastream200ResponseData.to_json())

# convert the object into a dict
get_datastream200_response_data_dict = get_datastream200_response_data_instance.to_dict()
# create an instance of GetDatastream200ResponseData from a dict
get_datastream200_response_data_from_dict = GetDatastream200ResponseData.from_dict(get_datastream200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


