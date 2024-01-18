# GetDatastream200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**GetDatastream200ResponseData**](GetDatastream200ResponseData.md) |  | [optional] 

## Example

```python
from sensorbucket.models.get_datastream200_response import GetDatastream200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatastream200Response from a JSON string
get_datastream200_response_instance = GetDatastream200Response.from_json(json)
# print the JSON string representation of the object
print GetDatastream200Response.to_json()

# convert the object into a dict
get_datastream200_response_dict = get_datastream200_response_instance.to_dict()
# create an instance of GetDatastream200Response from a dict
get_datastream200_response_form_dict = get_datastream200_response.from_dict(get_datastream200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


