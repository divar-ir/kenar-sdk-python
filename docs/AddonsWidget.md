# AddonsWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_bar** | [**AddonsButtonBar**](AddonsButtonBar.md) |  | [optional] 
**description_row** | [**AddonsDescriptionRow**](AddonsDescriptionRow.md) |  | [optional] 
**evaluation_row** | [**AddonsEvaluationRow**](AddonsEvaluationRow.md) |  | [optional] 
**event_row** | [**AddonsEventRow**](AddonsEventRow.md) |  | [optional] 
**group_info_row** | [**AddonsGroupInfoRow**](AddonsGroupInfoRow.md) |  | [optional] 
**image_carousel_row** | [**AddonsImageCarouselRow**](AddonsImageCarouselRow.md) |  | [optional] 
**score_row** | [**AddonsScoreRow**](AddonsScoreRow.md) |  | [optional] 
**selector_row** | [**AddonsSelectorRow**](AddonsSelectorRow.md) |  | [optional] 
**semantic_paths** | **Dict[str, str]** |  | [optional] 
**subtitle_row** | [**AddonsSubtitleRow**](AddonsSubtitleRow.md) |  | [optional] 
**title_row** | [**AddonsTitleRow**](AddonsTitleRow.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_widget import AddonsWidget

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsWidget from a JSON string
addons_widget_instance = AddonsWidget.from_json(json)
# print the JSON string representation of the object
print(AddonsWidget.to_json())

# convert the object into a dict
addons_widget_dict = addons_widget_instance.to_dict()
# create an instance of AddonsWidget from a dict
addons_widget_from_dict = AddonsWidget.from_dict(addons_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


