# PostApartmentSellFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floor** | **int** | Floor of the property. Use -1 for under ground floor and 0 for ground floor. Use 1 for first floor and so on. | 
**has_elevator** | **bool** | Whether the property has an elevator | 
**has_own_image** | **bool** | تصاویر مربوط به خود ملک بوده و تزئینی نیستند. | 
**has_parking** | **bool** | Whether the property has a parking | 
**has_warehouse** | **bool** | Whether the property has a warehouse | 
**price** | **str** | Price of the property in Toman | 
**rooms_count** | [**PostRoomsCount**](PostRoomsCount.md) |  | 
**size** | **int** | Size of the property in square meters | 
**year_built** | **int** | Year the property was built (Persian/Shamsi calendar) | 

## Example

```python
from kenar_api_client.models.post_apartment_sell_fields import PostApartmentSellFields

# TODO update the JSON string below
json = "{}"
# create an instance of PostApartmentSellFields from a JSON string
post_apartment_sell_fields_instance = PostApartmentSellFields.from_json(json)
# print the JSON string representation of the object
print(PostApartmentSellFields.to_json())

# convert the object into a dict
post_apartment_sell_fields_dict = post_apartment_sell_fields_instance.to_dict()
# create an instance of PostApartmentSellFields from a dict
post_apartment_sell_fields_from_dict = PostApartmentSellFields.from_dict(post_apartment_sell_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


