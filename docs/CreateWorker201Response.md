# CreateWorker201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**UserWorker**](UserWorker.md) |  | [optional] 

## Example

```python
from sensorbucket.models.create_worker201_response import CreateWorker201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorker201Response from a JSON string
create_worker201_response_instance = CreateWorker201Response.from_json(json)
# print the JSON string representation of the object
print CreateWorker201Response.to_json()

# convert the object into a dict
create_worker201_response_dict = create_worker201_response_instance.to_dict()
# create an instance of CreateWorker201Response from a dict
create_worker201_response_form_dict = create_worker201_response.from_dict(create_worker201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


