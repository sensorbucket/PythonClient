# UpdatePipeline200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**Pipeline**](Pipeline.md) |  | [optional] 

## Example

```python
from sensorbucket.models.update_pipeline200_response import UpdatePipeline200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePipeline200Response from a JSON string
update_pipeline200_response_instance = UpdatePipeline200Response.from_json(json)
# print the JSON string representation of the object
print UpdatePipeline200Response.to_json()

# convert the object into a dict
update_pipeline200_response_dict = update_pipeline200_response_instance.to_dict()
# create an instance of UpdatePipeline200Response from a dict
update_pipeline200_response_form_dict = update_pipeline200_response.from_dict(update_pipeline200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


