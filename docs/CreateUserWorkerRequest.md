# CreateUserWorkerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**user_code** | **str** | base64 encoded user code | 
**state** | **str** |  | [optional] 

## Example

```python
from sensorbucket.models.create_user_worker_request import CreateUserWorkerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserWorkerRequest from a JSON string
create_user_worker_request_instance = CreateUserWorkerRequest.from_json(json)
# print the JSON string representation of the object
print CreateUserWorkerRequest.to_json()

# convert the object into a dict
create_user_worker_request_dict = create_user_worker_request_instance.to_dict()
# create an instance of CreateUserWorkerRequest from a dict
create_user_worker_request_form_dict = create_user_worker_request.from_dict(create_user_worker_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


