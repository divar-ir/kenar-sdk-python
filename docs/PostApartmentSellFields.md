# PostApartmentSellFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**floor** | **int** | طبقه ملک. از -1 برای زیرزمین و 0 برای همکف استفاده کنید. از 1 برای طبقه اول و غیره. | 
**has_elevator** | **bool** | آیا ملک آسانسور دارد | 
**has_own_image** | **bool** | تصاویر مربوط به خود ملک بوده و تزئینی نیستند. | 
**has_parking** | **bool** | آیا ملک پارکینگ دارد | 
**has_warehouse** | **bool** | آیا ملک انباری دارد | 
**price** | **str** | قیمت ملک به تومان | 
**rooms_count** | [**PostRoomsCount**](PostRoomsCount.md) |  | 
**size** | **int** | مساحت ملک بر حسب متر مربع | 
**year_built** | **int** | سال ساخت ملک (تقویم شمسی) | 

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


