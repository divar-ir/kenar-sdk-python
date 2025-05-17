# AddonsAddonSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokens** | **List[str]** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**cities** | **List[str]** |  | [optional] 
**districts** | **List[str]** |  | [optional] 
**brand_models** | **List[str]** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_addon_selector import AddonsAddonSelector

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsAddonSelector from a JSON string
addons_addon_selector_instance = AddonsAddonSelector.from_json(json)
# print the JSON string representation of the object
print(AddonsAddonSelector.to_json())

# convert the object into a dict
addons_addon_selector_dict = addons_addon_selector_instance.to_dict()
# create an instance of AddonsAddonSelector from a dict
addons_addon_selector_from_dict = AddonsAddonSelector.from_dict(addons_addon_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


