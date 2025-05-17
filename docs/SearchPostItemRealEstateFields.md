# SearchPostItemRealEstateFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit** | [**SearchPostItemPrice**](SearchPostItemPrice.md) |  | [optional] 
**rent** | [**SearchPostItemPrice**](SearchPostItemPrice.md) |  | [optional] 
**daily_rent** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**has_parking** | **bool** |  | [optional] 
**has_elevator** | **bool** |  | [optional] 
**rooms** | **str** |  | [optional] 
**floor** | **int** |  | [optional] 

## Example

```python
from kenar_api_client.models.search_post_item_real_estate_fields import SearchPostItemRealEstateFields

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPostItemRealEstateFields from a JSON string
search_post_item_real_estate_fields_instance = SearchPostItemRealEstateFields.from_json(json)
# print the JSON string representation of the object
print(SearchPostItemRealEstateFields.to_json())

# convert the object into a dict
search_post_item_real_estate_fields_dict = search_post_item_real_estate_fields_instance.to_dict()
# create an instance of SearchPostItemRealEstateFields from a dict
search_post_item_real_estate_fields_from_dict = SearchPostItemRealEstateFields.from_dict(search_post_item_real_estate_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


