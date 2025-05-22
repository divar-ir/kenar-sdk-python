# AddonsGroupInfoRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_divider** | **bool** |  | [optional] 
**items** | [**List[AddonsGroupInfoRowGroupInfoItem]**](AddonsGroupInfoRowGroupInfoItem.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_group_info_row import AddonsGroupInfoRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsGroupInfoRow from a JSON string
addons_group_info_row_instance = AddonsGroupInfoRow.from_json(json)
# print the JSON string representation of the object
print(AddonsGroupInfoRow.to_json())

# convert the object into a dict
addons_group_info_row_dict = addons_group_info_row_instance.to_dict()
# create an instance of AddonsGroupInfoRow from a dict
addons_group_info_row_from_dict = AddonsGroupInfoRow.from_dict(addons_group_info_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


