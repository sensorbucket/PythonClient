# PaginatedResponseLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 

## Example

```python
from sensorbucket.models.paginated_response_links import PaginatedResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseLinks from a JSON string
paginated_response_links_instance = PaginatedResponseLinks.from_json(json)
# print the JSON string representation of the object
print PaginatedResponseLinks.to_json()

# convert the object into a dict
paginated_response_links_dict = paginated_response_links_instance.to_dict()
# create an instance of PaginatedResponseLinks from a dict
paginated_response_links_form_dict = paginated_response_links.from_dict(paginated_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


