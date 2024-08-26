# ListApiKeys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedResponseLinks**](PaginatedResponseLinks.md) |  | 
**page_size** | **int** |  | 
**total_count** | **int** |  | 
**data** | [**List[ApiKey]**](ApiKey.md) |  | 

## Example

```python
from sensorbucket.models.list_api_keys200_response import ListApiKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListApiKeys200Response from a JSON string
list_api_keys200_response_instance = ListApiKeys200Response.from_json(json)
# print the JSON string representation of the object
print(ListApiKeys200Response.to_json())

# convert the object into a dict
list_api_keys200_response_dict = list_api_keys200_response_instance.to_dict()
# create an instance of ListApiKeys200Response from a dict
list_api_keys200_response_from_dict = ListApiKeys200Response.from_dict(list_api_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


