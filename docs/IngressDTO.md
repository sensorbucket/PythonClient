# IngressDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracing_id** | **str** |  | 
**pipeline_id** | **str** |  | 
**owner_id** | **int** |  | 
**payload** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from sensorbucket.models.ingress_dto import IngressDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IngressDTO from a JSON string
ingress_dto_instance = IngressDTO.from_json(json)
# print the JSON string representation of the object
print(IngressDTO.to_json())

# convert the object into a dict
ingress_dto_dict = ingress_dto_instance.to_dict()
# create an instance of IngressDTO from a dict
ingress_dto_from_dict = IngressDTO.from_dict(ingress_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


