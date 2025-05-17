# AssetsGetServiceTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_types** | [**List[GetServiceTypesResponseServiceTypeData]**](GetServiceTypesResponseServiceTypeData.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_service_types_response import AssetsGetServiceTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetServiceTypesResponse from a JSON string
assets_get_service_types_response_instance = AssetsGetServiceTypesResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetServiceTypesResponse.to_json())

# convert the object into a dict
assets_get_service_types_response_dict = assets_get_service_types_response_instance.to_dict()
# create an instance of AssetsGetServiceTypesResponse from a dict
assets_get_service_types_response_from_dict = AssetsGetServiceTypesResponse.from_dict(assets_get_service_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


