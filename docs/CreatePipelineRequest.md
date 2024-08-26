# CreatePipelineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**steps** | **List[str]** |  | [optional] 

## Example

```python
from sensorbucket.models.create_pipeline_request import CreatePipelineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePipelineRequest from a JSON string
create_pipeline_request_instance = CreatePipelineRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePipelineRequest.to_json())

# convert the object into a dict
create_pipeline_request_dict = create_pipeline_request_instance.to_dict()
# create an instance of CreatePipelineRequest from a dict
create_pipeline_request_from_dict = CreatePipelineRequest.from_dict(create_pipeline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


