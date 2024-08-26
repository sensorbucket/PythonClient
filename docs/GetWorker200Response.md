# GetWorker200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**UserWorker**](UserWorker.md) |  | [optional] 

## Example

```python
from sensorbucket.models.get_worker200_response import GetWorker200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorker200Response from a JSON string
get_worker200_response_instance = GetWorker200Response.from_json(json)
# print the JSON string representation of the object
print(GetWorker200Response.to_json())

# convert the object into a dict
get_worker200_response_dict = get_worker200_response_instance.to_dict()
# create an instance of GetWorker200Response from a dict
get_worker200_response_from_dict = GetWorker200Response.from_dict(get_worker200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


