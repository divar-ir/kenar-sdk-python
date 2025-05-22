# AddonsAddonMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**AppsApp**](AppsApp.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 
**service_tags** | [**List[AppsServiceTag]**](AppsServiceTag.md) |  | [optional] 
**status** | [**AddonsStatus**](AddonsStatus.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_addon_meta_data import AddonsAddonMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsAddonMetaData from a JSON string
addons_addon_meta_data_instance = AddonsAddonMetaData.from_json(json)
# print the JSON string representation of the object
print(AddonsAddonMetaData.to_json())

# convert the object into a dict
addons_addon_meta_data_dict = addons_addon_meta_data_instance.to_dict()
# create an instance of AddonsAddonMetaData from a dict
addons_addon_meta_data_from_dict = AddonsAddonMetaData.from_dict(addons_addon_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


