# AddonsPostAddon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**AppsApp**](AppsApp.md) |  | [optional] 
**linkage** | [**AddonsAddonLinkage**](AddonsAddonLinkage.md) |  | [optional] 
**meta_data** | [**AddonsAddonMetaData**](AddonsAddonMetaData.md) |  | [optional] 
**score** | **str** |  | [optional] 
**secondary_links** | [**AddonsAddonSecondaryLinks**](AddonsAddonSecondaryLinks.md) |  | [optional] 
**selector** | [**AddonsAddonSelector**](AddonsAddonSelector.md) |  | [optional] 
**semantic** | **Dict[str, str]** |  | [optional] 
**semantic_data** | [**AddonsAddonSemantic**](AddonsAddonSemantic.md) |  | [optional] 
**semantic_sensitives** | **List[str]** |  | [optional] 
**sensitive_semantic** | **Dict[str, str]** |  | [optional] 
**token** | **str** |  | [optional] 
**widgets** | **object** |  | [optional] 
**widgets_semantic** | **object** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_post_addon import AddonsPostAddon

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsPostAddon from a JSON string
addons_post_addon_instance = AddonsPostAddon.from_json(json)
# print the JSON string representation of the object
print(AddonsPostAddon.to_json())

# convert the object into a dict
addons_post_addon_dict = addons_post_addon_instance.to_dict()
# create an instance of AddonsPostAddon from a dict
addons_post_addon_from_dict = AddonsPostAddon.from_dict(addons_post_addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


