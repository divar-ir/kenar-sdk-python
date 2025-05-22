# AddonsBusinessAddon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_ref** | **str** |  | [optional] 
**meta_data** | [**AddonsAddonMetaData**](AddonsAddonMetaData.md) |  | [optional] 
**widgets** | **object** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_business_addon import AddonsBusinessAddon

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsBusinessAddon from a JSON string
addons_business_addon_instance = AddonsBusinessAddon.from_json(json)
# print the JSON string representation of the object
print(AddonsBusinessAddon.to_json())

# convert the object into a dict
addons_business_addon_dict = addons_business_addon_instance.to_dict()
# create an instance of AddonsBusinessAddon from a dict
addons_business_addon_from_dict = AddonsBusinessAddon.from_dict(addons_business_addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


