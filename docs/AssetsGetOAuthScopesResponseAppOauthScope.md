# AssetsGetOAuthScopesResponseAppOauthScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display** | **str** |  | [optional] 
**lifecycle_state** | [**AssetsGetOAuthScopesResponseLifeCycleState**](AssetsGetOAuthScopesResponseLifeCycleState.md) |  | [optional] 
**slug** | [**OAuthScopeScope**](OAuthScopeScope.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_o_auth_scopes_response_app_oauth_scope import AssetsGetOAuthScopesResponseAppOauthScope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetOAuthScopesResponseAppOauthScope from a JSON string
assets_get_o_auth_scopes_response_app_oauth_scope_instance = AssetsGetOAuthScopesResponseAppOauthScope.from_json(json)
# print the JSON string representation of the object
print(AssetsGetOAuthScopesResponseAppOauthScope.to_json())

# convert the object into a dict
assets_get_o_auth_scopes_response_app_oauth_scope_dict = assets_get_o_auth_scopes_response_app_oauth_scope_instance.to_dict()
# create an instance of AssetsGetOAuthScopesResponseAppOauthScope from a dict
assets_get_o_auth_scopes_response_app_oauth_scope_from_dict = AssetsGetOAuthScopesResponseAppOauthScope.from_dict(assets_get_o_auth_scopes_response_app_oauth_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


