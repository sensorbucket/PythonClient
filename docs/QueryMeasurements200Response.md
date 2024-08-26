# QueryMeasurements200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedResponseLinks**](PaginatedResponseLinks.md) |  | 
**page_size** | **int** |  | 
**total_count** | **int** |  | 
**data** | [**List[Measurement]**](Measurement.md) |  | 

## Example

```python
from sensorbucket.models.query_measurements200_response import QueryMeasurements200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMeasurements200Response from a JSON string
query_measurements200_response_instance = QueryMeasurements200Response.from_json(json)
# print the JSON string representation of the object
print(QueryMeasurements200Response.to_json())

# convert the object into a dict
query_measurements200_response_dict = query_measurements200_response_instance.to_dict()
# create an instance of QueryMeasurements200Response from a dict
query_measurements200_response_from_dict = QueryMeasurements200Response.from_dict(query_measurements200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


