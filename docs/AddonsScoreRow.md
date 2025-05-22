# AddonsScoreRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AddonsAction**](AddonsAction.md) |  | [optional] 
**descriptive_score** | **str** |  | [optional] 
**has_divider** | **bool** |  | [optional] 
**icon_name** | [**DivarIconsIconName**](DivarIconsIconName.md) |  | [optional] 
**percentage_score** | **int** |  | [optional] 
**score_color** | [**AddonsWidgetColor**](AddonsWidgetColor.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_score_row import AddonsScoreRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsScoreRow from a JSON string
addons_score_row_instance = AddonsScoreRow.from_json(json)
# print the JSON string representation of the object
print(AddonsScoreRow.to_json())

# convert the object into a dict
addons_score_row_dict = addons_score_row_instance.to_dict()
# create an instance of AddonsScoreRow from a dict
addons_score_row_from_dict = AddonsScoreRow.from_dict(addons_score_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


