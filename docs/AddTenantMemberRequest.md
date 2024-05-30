# AddTenantMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**permissions** | **List[str]** |  | 

## Example

```python
from sensorbucket.models.add_tenant_member_request import AddTenantMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTenantMemberRequest from a JSON string
add_tenant_member_request_instance = AddTenantMemberRequest.from_json(json)
# print the JSON string representation of the object
print AddTenantMemberRequest.to_json()

# convert the object into a dict
add_tenant_member_request_dict = add_tenant_member_request_instance.to_dict()
# create an instance of AddTenantMemberRequest from a dict
add_tenant_member_request_form_dict = add_tenant_member_request.from_dict(add_tenant_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


