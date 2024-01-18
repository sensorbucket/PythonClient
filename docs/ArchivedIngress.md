# ArchivedIngress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** |  | 
**raw_message** | **str** |  | 
**archived_at** | **datetime** |  | 
**expires_at** | **datetime** |  | 
**ingress_dto** | [**IngressDTO**](IngressDTO.md) |  | [optional] 

## Example

```python
from sensorbucket.models.archived_ingress import ArchivedIngress

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivedIngress from a JSON string
archived_ingress_instance = ArchivedIngress.from_json(json)
# print the JSON string representation of the object
print ArchivedIngress.to_json()

# convert the object into a dict
archived_ingress_dict = archived_ingress_instance.to_dict()
# create an instance of ArchivedIngress from a dict
archived_ingress_form_dict = archived_ingress.from_dict(archived_ingress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


