# ListTenants200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedResponseLinks**](PaginatedResponseLinks.md) |  | 
**page_size** | **int** |  | 
**total_count** | **int** |  | 
**data** | [**List[Tenant]**](Tenant.md) |  | 

## Example

```python
from sensorbucket.models.list_tenants200_response import ListTenants200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTenants200Response from a JSON string
list_tenants200_response_instance = ListTenants200Response.from_json(json)
# print the JSON string representation of the object
print ListTenants200Response.to_json()

# convert the object into a dict
list_tenants200_response_dict = list_tenants200_response_instance.to_dict()
# create an instance of ListTenants200Response from a dict
list_tenants200_response_form_dict = list_tenants200_response.from_dict(list_tenants200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


