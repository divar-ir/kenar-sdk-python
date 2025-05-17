# AssetsGetOAuthScopesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | [**List[AssetsGetOAuthScopesResponseAppOauthScope]**](AssetsGetOAuthScopesResponseAppOauthScope.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_o_auth_scopes_response import AssetsGetOAuthScopesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetOAuthScopesResponse from a JSON string
assets_get_o_auth_scopes_response_instance = AssetsGetOAuthScopesResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetOAuthScopesResponse.to_json())

# convert the object into a dict
assets_get_o_auth_scopes_response_dict = assets_get_o_auth_scopes_response_instance.to_dict()
# create an instance of AssetsGetOAuthScopesResponse from a dict
assets_get_o_auth_scopes_response_from_dict = AssetsGetOAuthScopesResponse.from_dict(assets_get_o_auth_scopes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


