# GetServiceTypesResponseServiceTypeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** |  | [optional] 
**slug** | [**AppsServiceType**](AppsServiceType.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.get_service_types_response_service_type_data import GetServiceTypesResponseServiceTypeData

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceTypesResponseServiceTypeData from a JSON string
get_service_types_response_service_type_data_instance = GetServiceTypesResponseServiceTypeData.from_json(json)
# print the JSON string representation of the object
print(GetServiceTypesResponseServiceTypeData.to_json())

# convert the object into a dict
get_service_types_response_service_type_data_dict = get_service_types_response_service_type_data_instance.to_dict()
# create an instance of GetServiceTypesResponseServiceTypeData from a dict
get_service_types_response_service_type_data_from_dict = GetServiceTypesResponseServiceTypeData.from_dict(get_service_types_response_service_type_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


