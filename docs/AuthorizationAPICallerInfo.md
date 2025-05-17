# AuthorizationAPICallerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **int** |  | [optional] 
**app** | [**AppsApp**](AppsApp.md) |  | [optional] 
**scopes** | [**List[AuthorizationOAuthScope]**](AuthorizationOAuthScope.md) |  | [optional] 
**api_key_id_v2** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.authorization_api_caller_info import AuthorizationAPICallerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationAPICallerInfo from a JSON string
authorization_api_caller_info_instance = AuthorizationAPICallerInfo.from_json(json)
# print the JSON string representation of the object
print(AuthorizationAPICallerInfo.to_json())

# convert the object into a dict
authorization_api_caller_info_dict = authorization_api_caller_info_instance.to_dict()
# create an instance of AuthorizationAPICallerInfo from a dict
authorization_api_caller_info_from_dict = AuthorizationAPICallerInfo.from_dict(authorization_api_caller_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


