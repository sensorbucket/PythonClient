# UpdatePipelineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**steps** | **List[str]** |  | [optional] 
**status** | **str** | Used to change a pipeline from inactive to active or vice-versa.  Moving from active to inactive can also be achieve by &#x60;DELETE&#x60;ing the pipeline resource.  | [optional] 

## Example

```python
from sensorbucket.models.update_pipeline_request import UpdatePipelineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePipelineRequest from a JSON string
update_pipeline_request_instance = UpdatePipelineRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePipelineRequest.to_json()

# convert the object into a dict
update_pipeline_request_dict = update_pipeline_request_instance.to_dict()
# create an instance of UpdatePipelineRequest from a dict
update_pipeline_request_form_dict = update_pipeline_request.from_dict(update_pipeline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


