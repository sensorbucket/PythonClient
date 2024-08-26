# UserWorker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**state** | **str** |  | 
**language** | **str** |  | 
**tenant_id** | **int** |  | [optional] 
**revision** | **int** |  | 
**status** | **str** |  | 

## Example

```python
from sensorbucket.models.user_worker import UserWorker

# TODO update the JSON string below
json = "{}"
# create an instance of UserWorker from a JSON string
user_worker_instance = UserWorker.from_json(json)
# print the JSON string representation of the object
print UserWorker.to_json()

# convert the object into a dict
user_worker_dict = user_worker_instance.to_dict()
# create an instance of UserWorker from a dict
user_worker_form_dict = user_worker.from_dict(user_worker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


