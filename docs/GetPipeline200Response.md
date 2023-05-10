# GetPipeline200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**Pipeline**](Pipeline.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_pipeline200_response import GetPipeline200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPipeline200Response from a JSON string
get_pipeline200_response_instance = GetPipeline200Response.from_json(json)
# print the JSON string representation of the object
print GetPipeline200Response.to_json()

# convert the object into a dict
get_pipeline200_response_dict = get_pipeline200_response_instance.to_dict()
# create an instance of GetPipeline200Response from a dict
get_pipeline200_response_form_dict = get_pipeline200_response.from_dict(get_pipeline200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


