# Sensor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**archive_time** | **float** |  | [optional] 
**properties** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from sensorbucket.models.sensor import Sensor

# TODO update the JSON string below
json = "{}"
# create an instance of Sensor from a JSON string
sensor_instance = Sensor.from_json(json)
# print the JSON string representation of the object
print Sensor.to_json()

# convert the object into a dict
sensor_dict = sensor_instance.to_dict()
# create an instance of Sensor from a dict
sensor_form_dict = sensor.from_dict(sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


