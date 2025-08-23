# OpenPlatformpostServicesFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**PostServicesFieldsCategory**](PostServicesFieldsCategory.md) |  | 
**expertise_ids** | **List[str]** | List of expertise ids | 
**work_hours_end** | **int** | End hour of work in 24-hour format (e.g. 18 for 18:00). Only applicable if &#x60;works_24_7&#x60; is false. | 
**work_hours_start** | **int** | Start hour of work in 24-hour format (e.g. 9 for 9:00). Only applicable if &#x60;works_24_7&#x60; is false. | 
**work_on_holidays** | **bool** | Whether the service provider works on holidays | 
**works_24_7** | **bool** | Whether the service provider is available 24/7. If true, &#x60;work_hours_start&#x60; and &#x60;work_hours_end&#x60; are ignored. | 

## Example

```python
from kenar_api_client.models.open_platformpost_services_fields import OpenPlatformpostServicesFields

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPlatformpostServicesFields from a JSON string
open_platformpost_services_fields_instance = OpenPlatformpostServicesFields.from_json(json)
# print the JSON string representation of the object
print(OpenPlatformpostServicesFields.to_json())

# convert the object into a dict
open_platformpost_services_fields_dict = open_platformpost_services_fields_instance.to_dict()
# create an instance of OpenPlatformpostServicesFields from a dict
open_platformpost_services_fields_from_dict = OpenPlatformpostServicesFields.from_dict(open_platformpost_services_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


