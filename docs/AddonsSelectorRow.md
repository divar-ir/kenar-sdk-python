# AddonsSelectorRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AddonsAction**](AddonsAction.md) |  | [optional] 
**has_divider** | **bool** |  | [optional] 
**icon_name** | [**DivarIconsIconName**](DivarIconsIconName.md) |  | [optional] 
**image_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_selector_row import AddonsSelectorRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsSelectorRow from a JSON string
addons_selector_row_instance = AddonsSelectorRow.from_json(json)
# print the JSON string representation of the object
print(AddonsSelectorRow.to_json())

# convert the object into a dict
addons_selector_row_dict = addons_selector_row_instance.to_dict()
# create an instance of AddonsSelectorRow from a dict
addons_selector_row_from_dict = AddonsSelectorRow.from_dict(addons_selector_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


