# AddonsGetPostAddonsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[AddonsPostAddon]**](AddonsPostAddon.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_get_post_addons_response import AddonsGetPostAddonsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsGetPostAddonsResponse from a JSON string
addons_get_post_addons_response_instance = AddonsGetPostAddonsResponse.from_json(json)
# print the JSON string representation of the object
print(AddonsGetPostAddonsResponse.to_json())

# convert the object into a dict
addons_get_post_addons_response_dict = addons_get_post_addons_response_instance.to_dict()
# create an instance of AddonsGetPostAddonsResponse from a dict
addons_get_post_addons_response_from_dict = AddonsGetPostAddonsResponse.from_dict(addons_get_post_addons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


