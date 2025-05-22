# FinderSearchPostItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**community_fields** | **object** |  | [optional] 
**electronic_devices_fields** | **object** |  | [optional] 
**home_kitchen_fields** | **object** |  | [optional] 
**jobs_fields** | **object** |  | [optional] 
**last_modified_at** | **datetime** |  | [optional] 
**leisure_hobbies_fields** | **object** |  | [optional] 
**personal_goods_fields** | **object** |  | [optional] 
**price** | [**SearchPostItemPrice**](SearchPostItemPrice.md) |  | [optional] 
**real_estate_fields** | [**SearchPostItemRealEstateFields**](SearchPostItemRealEstateFields.md) |  | [optional] 
**services_fields** | **object** |  | [optional] 
**title** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**tools_materials_equipment_fields** | **object** |  | [optional] 
**vehicles_fields** | [**SearchPostItemVehiclesFields**](SearchPostItemVehiclesFields.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_search_post_item import FinderSearchPostItem

# TODO update the JSON string below
json = "{}"
# create an instance of FinderSearchPostItem from a JSON string
finder_search_post_item_instance = FinderSearchPostItem.from_json(json)
# print the JSON string representation of the object
print(FinderSearchPostItem.to_json())

# convert the object into a dict
finder_search_post_item_dict = finder_search_post_item_instance.to_dict()
# create an instance of FinderSearchPostItem from a dict
finder_search_post_item_from_dict = FinderSearchPostItem.from_dict(finder_search_post_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


