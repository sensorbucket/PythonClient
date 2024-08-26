# UpdateTenantMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | 

## Example

```python
from sensorbucket.models.update_tenant_member_request import UpdateTenantMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantMemberRequest from a JSON string
update_tenant_member_request_instance = UpdateTenantMemberRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantMemberRequest.to_json())

# convert the object into a dict
update_tenant_member_request_dict = update_tenant_member_request_instance.to_dict()
# create an instance of UpdateTenantMemberRequest from a dict
update_tenant_member_request_from_dict = UpdateTenantMemberRequest.from_dict(update_tenant_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


