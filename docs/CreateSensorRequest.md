# CreateSensorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**description** | **str** |  | [optional] 
**external_id** | **str** |  | 
**brand** | **str** |  | [optional] 
**properties** | **object** |  | [optional] 
**archive_time** | **int** |  | [optional] 

## Example

```python
from sensorbucket.models.create_sensor_request import CreateSensorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSensorRequest from a JSON string
create_sensor_request_instance = CreateSensorRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSensorRequest.to_json())

# convert the object into a dict
create_sensor_request_dict = create_sensor_request_instance.to_dict()
# create an instance of CreateSensorRequest from a dict
create_sensor_request_from_dict = CreateSensorRequest.from_dict(create_sensor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


