# AddonsEventRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**has_divider** | **bool** |  | [optional] 
**icon_name** | [**DivarIconsIconName**](DivarIconsIconName.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_event_row import AddonsEventRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsEventRow from a JSON string
addons_event_row_instance = AddonsEventRow.from_json(json)
# print the JSON string representation of the object
print(AddonsEventRow.to_json())

# convert the object into a dict
addons_event_row_dict = addons_event_row_instance.to_dict()
# create an instance of AddonsEventRow from a dict
addons_event_row_from_dict = AddonsEventRow.from_dict(addons_event_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


