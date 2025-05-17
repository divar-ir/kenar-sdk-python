# AddonsUserAddon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_data** | [**AddonsAddonMetaData**](AddonsAddonMetaData.md) |  | [optional] 
**phone** | **str** |  | [optional] 
**divar_user_id** | **str** |  | [optional] 
**widgets** | **object** |  | [optional] 
**semantic** | **Dict[str, str]** |  | [optional] 
**semantic_data** | [**AddonsAddonSemantic**](AddonsAddonSemantic.md) |  | [optional] 
**sensitive_semantic** | **Dict[str, str]** |  | [optional] 
**widgets_semantic** | **object** |  | [optional] 
**filters** | [**AddonsUserAddonFilters**](AddonsUserAddonFilters.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_user_addon import AddonsUserAddon

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsUserAddon from a JSON string
addons_user_addon_instance = AddonsUserAddon.from_json(json)
# print the JSON string representation of the object
print(AddonsUserAddon.to_json())

# convert the object into a dict
addons_user_addon_dict = addons_user_addon_instance.to_dict()
# create an instance of AddonsUserAddon from a dict
addons_user_addon_from_dict = AddonsUserAddon.from_dict(addons_user_addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


