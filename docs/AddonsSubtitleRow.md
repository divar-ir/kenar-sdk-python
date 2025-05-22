# AddonsSubtitleRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_divider** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_subtitle_row import AddonsSubtitleRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsSubtitleRow from a JSON string
addons_subtitle_row_instance = AddonsSubtitleRow.from_json(json)
# print the JSON string representation of the object
print(AddonsSubtitleRow.to_json())

# convert the object into a dict
addons_subtitle_row_dict = addons_subtitle_row_instance.to_dict()
# create an instance of AddonsSubtitleRow from a dict
addons_subtitle_row_from_dict = AddonsSubtitleRow.from_dict(addons_subtitle_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


