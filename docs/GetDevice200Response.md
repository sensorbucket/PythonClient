# GetDevice200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**Device**](Device.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_device200_response import GetDevice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevice200Response from a JSON string
get_device200_response_instance = GetDevice200Response.from_json(json)
# print the JSON string representation of the object
print GetDevice200Response.to_json()

# convert the object into a dict
get_device200_response_dict = get_device200_response_instance.to_dict()
# create an instance of GetDevice200Response from a dict
get_device200_response_form_dict = get_device200_response.from_dict(get_device200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


