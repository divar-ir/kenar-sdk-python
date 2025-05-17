# SearchPostItemVehiclesFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | **str** |  | [optional] 
**installment_sale** | **str** |  | [optional] 
**custom_post_subtitle** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.search_post_item_vehicles_fields import SearchPostItemVehiclesFields

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPostItemVehiclesFields from a JSON string
search_post_item_vehicles_fields_instance = SearchPostItemVehiclesFields.from_json(json)
# print the JSON string representation of the object
print(SearchPostItemVehiclesFields.to_json())

# convert the object into a dict
search_post_item_vehicles_fields_dict = search_post_item_vehicles_fields_instance.to_dict()
# create an instance of SearchPostItemVehiclesFields from a dict
search_post_item_vehicles_fields_from_dict = SearchPostItemVehiclesFields.from_dict(search_post_item_vehicles_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


