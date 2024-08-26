# ListSensorGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedResponseLinks**](PaginatedResponseLinks.md) |  | 
**page_size** | **int** |  | 
**total_count** | **int** |  | 
**data** | [**List[SensorGroup]**](SensorGroup.md) |  | 

## Example

```python
from sensorbucket.models.list_sensor_groups200_response import ListSensorGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSensorGroups200Response from a JSON string
list_sensor_groups200_response_instance = ListSensorGroups200Response.from_json(json)
# print the JSON string representation of the object
print(ListSensorGroups200Response.to_json())

# convert the object into a dict
list_sensor_groups200_response_dict = list_sensor_groups200_response_instance.to_dict()
# create an instance of ListSensorGroups200Response from a dict
list_sensor_groups200_response_from_dict = ListSensorGroups200Response.from_dict(list_sensor_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


