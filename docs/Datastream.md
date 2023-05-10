# Datastream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**sensor_id** | **float** |  | [optional] 
**observed_property** | **str** |  | [optional] 
**unit_of_measurement** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.datastream import Datastream

# TODO update the JSON string below
json = "{}"
# create an instance of Datastream from a JSON string
datastream_instance = Datastream.from_json(json)
# print the JSON string representation of the object
print Datastream.to_json()

# convert the object into a dict
datastream_dict = datastream_instance.to_dict()
# create an instance of Datastream from a dict
datastream_form_dict = datastream.from_dict(datastream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


