# TraceStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | [optional] 
**status** | **int** |  | 
**status_string** | **str** |  | 
**duration** | **float** | Duration in seconds | 
**error** | **str** |  | 

## Example

```python
from sensorbucket.models.trace_step import TraceStep

# TODO update the JSON string below
json = "{}"
# create an instance of TraceStep from a JSON string
trace_step_instance = TraceStep.from_json(json)
# print the JSON string representation of the object
print(TraceStep.to_json())

# convert the object into a dict
trace_step_dict = trace_step_instance.to_dict()
# create an instance of TraceStep from a dict
trace_step_from_dict = TraceStep.from_dict(trace_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


