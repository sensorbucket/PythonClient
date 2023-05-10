# ListDeviceSensors200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedResponseLinks**](PaginatedResponseLinks.md) |  | 
**page_size** | **int** |  | 
**total_count** | **int** |  | 
**data** | [**List[Sensor]**](Sensor.md) |  | 

## Example

```python
from openapi_client.models.list_device_sensors200_response import ListDeviceSensors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeviceSensors200Response from a JSON string
list_device_sensors200_response_instance = ListDeviceSensors200Response.from_json(json)
# print the JSON string representation of the object
print ListDeviceSensors200Response.to_json()

# convert the object into a dict
list_device_sensors200_response_dict = list_device_sensors200_response_instance.to_dict()
# create an instance of ListDeviceSensors200Response from a dict
list_device_sensors200_response_form_dict = list_device_sensors200_response.from_dict(list_device_sensors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


