# UpdateWorkerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**user_code** | **str** | base64 encoded user code | [optional] 

## Example

```python
from sensorbucket.models.update_worker_request import UpdateWorkerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkerRequest from a JSON string
update_worker_request_instance = UpdateWorkerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkerRequest.to_json())

# convert the object into a dict
update_worker_request_dict = update_worker_request_instance.to_dict()
# create an instance of UpdateWorkerRequest from a dict
update_worker_request_from_dict = UpdateWorkerRequest.from_dict(update_worker_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


