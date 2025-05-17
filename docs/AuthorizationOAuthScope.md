# AuthorizationOAuthScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | [optional] 
**scope** | [**OAuthScopeScope**](OAuthScopeScope.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.authorization_o_auth_scope import AuthorizationOAuthScope

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationOAuthScope from a JSON string
authorization_o_auth_scope_instance = AuthorizationOAuthScope.from_json(json)
# print the JSON string representation of the object
print(AuthorizationOAuthScope.to_json())

# convert the object into a dict
authorization_o_auth_scope_dict = authorization_o_auth_scope_instance.to_dict()
# create an instance of AuthorizationOAuthScope from a dict
authorization_o_auth_scope_from_dict = AuthorizationOAuthScope.from_dict(authorization_o_auth_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


