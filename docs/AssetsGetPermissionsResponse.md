# AssetsGetPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[AssetsGetPermissionsResponsePermission]**](AssetsGetPermissionsResponsePermission.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_permissions_response import AssetsGetPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetPermissionsResponse from a JSON string
assets_get_permissions_response_instance = AssetsGetPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetPermissionsResponse.to_json())

# convert the object into a dict
assets_get_permissions_response_dict = assets_get_permissions_response_instance.to_dict()
# create an instance of AssetsGetPermissionsResponse from a dict
assets_get_permissions_response_from_dict = AssetsGetPermissionsResponse.from_dict(assets_get_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


