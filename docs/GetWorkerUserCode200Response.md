# GetWorkerUserCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | **str** | The usercode base64 encoded | [optional] 

## Example

```python
from sensorbucket.models.get_worker_user_code200_response import GetWorkerUserCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkerUserCode200Response from a JSON string
get_worker_user_code200_response_instance = GetWorkerUserCode200Response.from_json(json)
# print the JSON string representation of the object
print(GetWorkerUserCode200Response.to_json())

# convert the object into a dict
get_worker_user_code200_response_dict = get_worker_user_code200_response_instance.to_dict()
# create an instance of GetWorkerUserCode200Response from a dict
get_worker_user_code200_response_from_dict = GetWorkerUserCode200Response.from_dict(get_worker_user_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


