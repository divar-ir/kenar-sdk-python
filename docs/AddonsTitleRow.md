# AddonsTitleRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_divider** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_title_row import AddonsTitleRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsTitleRow from a JSON string
addons_title_row_instance = AddonsTitleRow.from_json(json)
# print the JSON string representation of the object
print(AddonsTitleRow.to_json())

# convert the object into a dict
addons_title_row_dict = addons_title_row_instance.to_dict()
# create an instance of AddonsTitleRow from a dict
addons_title_row_from_dict = AddonsTitleRow.from_dict(addons_title_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


