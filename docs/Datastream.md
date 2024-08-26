# Datastream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | 
**sensor_id** | **int** |  | 
**observed_property** | **str** |  | 
**unit_of_measurement** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from sensorbucket.models.datastream import Datastream

# TODO update the JSON string below
json = "{}"
# create an instance of Datastream from a JSON string
datastream_instance = Datastream.from_json(json)
# print the JSON string representation of the object
print(Datastream.to_json())

# convert the object into a dict
datastream_dict = datastream_instance.to_dict()
# create an instance of Datastream from a dict
datastream_from_dict = Datastream.from_dict(datastream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


