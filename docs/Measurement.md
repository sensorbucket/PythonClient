# Measurement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measurement_id** | **int** |  | 
**uplink_message_id** | **str** |  | 
**device_id** | **int** |  | 
**device_code** | **str** |  | 
**device_description** | **str** |  | [optional] 
**device_latitude** | **float** |  | [optional] 
**device_longitude** | **float** |  | [optional] 
**device_altitude** | **float** |  | [optional] 
**device_location_description** | **str** |  | [optional] 
**device_properties** | **object** |  | [optional] 
**device_state** | **int** |  | 
**sensor_id** | **int** |  | 
**sensor_code** | **str** |  | 
**sensor_description** | **str** |  | [optional] 
**sensor_external_id** | **str** |  | 
**sensor_properties** | **object** |  | [optional] 
**sensor_brand** | **str** |  | [optional] 
**sensor_archive_time** | **int** |  | [optional] 
**datastream_id** | **str** |  | 
**datastream_description** | **str** |  | [optional] 
**datastream_observed_property** | **str** |  | 
**datastream_unit_of_measurement** | **str** |  | 
**measurement_timestamp** | **datetime** |  | 
**measurement_value** | **float** |  | 
**measurement_latitude** | **float** |  | [optional] 
**measurement_longitude** | **float** |  | [optional] 
**measurement_altitude** | **float** |  | [optional] 
**measurement_properties** | **object** |  | [optional] 
**measurement_expiration** | **datetime** |  | 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from sensorbucket.models.measurement import Measurement

# TODO update the JSON string below
json = "{}"
# create an instance of Measurement from a JSON string
measurement_instance = Measurement.from_json(json)
# print the JSON string representation of the object
print(Measurement.to_json())

# convert the object into a dict
measurement_dict = measurement_instance.to_dict()
# create an instance of Measurement from a dict
measurement_from_dict = Measurement.from_dict(measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


