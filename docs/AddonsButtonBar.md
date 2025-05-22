# AddonsButtonBar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AddonsAction**](AddonsAction.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_button_bar import AddonsButtonBar

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsButtonBar from a JSON string
addons_button_bar_instance = AddonsButtonBar.from_json(json)
# print the JSON string representation of the object
print(AddonsButtonBar.to_json())

# convert the object into a dict
addons_button_bar_dict = addons_button_bar_instance.to_dict()
# create an instance of AddonsButtonBar from a dict
addons_button_bar_from_dict = AddonsButtonBar.from_dict(addons_button_bar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


