# CreateDevice201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**data** | [**Device**](Device.md) |  | [optional] 

## Example

```python
from sensorbucket.models.create_device201_response import CreateDevice201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDevice201Response from a JSON string
create_device201_response_instance = CreateDevice201Response.from_json(json)
# print the JSON string representation of the object
print(CreateDevice201Response.to_json())

# convert the object into a dict
create_device201_response_dict = create_device201_response_instance.to_dict()
# create an instance of CreateDevice201Response from a dict
create_device201_response_from_dict = CreateDevice201Response.from_dict(create_device201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


