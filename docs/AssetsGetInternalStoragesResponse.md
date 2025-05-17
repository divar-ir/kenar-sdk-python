# AssetsGetInternalStoragesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_storages** | [**List[AssetsEnumOption]**](AssetsEnumOption.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_internal_storages_response import AssetsGetInternalStoragesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetInternalStoragesResponse from a JSON string
assets_get_internal_storages_response_instance = AssetsGetInternalStoragesResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetInternalStoragesResponse.to_json())

# convert the object into a dict
assets_get_internal_storages_response_dict = assets_get_internal_storages_response_instance.to_dict()
# create an instance of AssetsGetInternalStoragesResponse from a dict
assets_get_internal_storages_response_from_dict = AssetsGetInternalStoragesResponse.from_dict(assets_get_internal_storages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


