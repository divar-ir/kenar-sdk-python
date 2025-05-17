# AddonsDescriptionRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**has_divider** | **bool** |  | [optional] 
**expandable** | **bool** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_description_row import AddonsDescriptionRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsDescriptionRow from a JSON string
addons_description_row_instance = AddonsDescriptionRow.from_json(json)
# print the JSON string representation of the object
print(AddonsDescriptionRow.to_json())

# convert the object into a dict
addons_description_row_dict = addons_description_row_instance.to_dict()
# create an instance of AddonsDescriptionRow from a dict
addons_description_row_from_dict = AddonsDescriptionRow.from_dict(addons_description_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


