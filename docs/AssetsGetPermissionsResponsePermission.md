# AssetsGetPermissionsResponsePermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display** | **str** |  | [optional] 
**lifecycle_state** | [**AssetsGetPermissionsResponseLifeCycleState**](AssetsGetPermissionsResponseLifeCycleState.md) |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_permissions_response_permission import AssetsGetPermissionsResponsePermission

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetPermissionsResponsePermission from a JSON string
assets_get_permissions_response_permission_instance = AssetsGetPermissionsResponsePermission.from_json(json)
# print the JSON string representation of the object
print(AssetsGetPermissionsResponsePermission.to_json())

# convert the object into a dict
assets_get_permissions_response_permission_dict = assets_get_permissions_response_permission_instance.to_dict()
# create an instance of AssetsGetPermissionsResponsePermission from a dict
assets_get_permissions_response_permission_from_dict = AssetsGetPermissionsResponsePermission.from_dict(assets_get_permissions_response_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


