# ListWorkers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedResponseLinks**](PaginatedResponseLinks.md) |  | 
**page_size** | **int** |  | 
**total_count** | **int** |  | 
**data** | [**List[UserWorker]**](UserWorker.md) |  | 

## Example

```python
from sensorbucket.models.list_workers200_response import ListWorkers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkers200Response from a JSON string
list_workers200_response_instance = ListWorkers200Response.from_json(json)
# print the JSON string representation of the object
print ListWorkers200Response.to_json()

# convert the object into a dict
list_workers200_response_dict = list_workers200_response_instance.to_dict()
# create an instance of ListWorkers200Response from a dict
list_workers200_response_form_dict = list_workers200_response.from_dict(list_workers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


