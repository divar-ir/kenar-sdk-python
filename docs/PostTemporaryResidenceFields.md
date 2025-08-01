# PostTemporaryResidenceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **int** | متراژ اقامتگاه به متر مربع | [optional] 
**extra_person_capacity** | **int** | تعداد افراد اضافه مجاز در اقامتگاه | [optional] 
**has_own_image** | **bool** | تصاویر مربوط به خود ملک بوده و تزئینی نیستند. | [optional] 
**price_cost_per_extra_person** | **str** | هزینه هر نفر اضافه به ازای هر شب به تومان | [optional] 
**price_regular_days** | **str** | قیمت اقامتگاه در روزهای عادی (شنبه تا سه‌شنبه) به تومان | [optional] 
**price_special_days** | **str** | قیمت اقامتگاه در روزهای خاص (تعطیلات و مناسبت‌ها) به تومان | [optional] 
**price_weekends** | **str** | قیمت اقامتگاه در آخر هفته (چهارشنبه تا جمعه) به تومان | [optional] 
**regular_person_capacity** | **int** | ظرفیت استاندارد افراد در اقامتگاه | [optional] 
**rooms_count** | [**TemporaryResidenceFieldsRoomsCount**](TemporaryResidenceFieldsRoomsCount.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.post_temporary_residence_fields import PostTemporaryResidenceFields

# TODO update the JSON string below
json = "{}"
# create an instance of PostTemporaryResidenceFields from a JSON string
post_temporary_residence_fields_instance = PostTemporaryResidenceFields.from_json(json)
# print the JSON string representation of the object
print(PostTemporaryResidenceFields.to_json())

# convert the object into a dict
post_temporary_residence_fields_dict = post_temporary_residence_fields_instance.to_dict()
# create an instance of PostTemporaryResidenceFields from a dict
post_temporary_residence_fields_from_dict = PostTemporaryResidenceFields.from_dict(post_temporary_residence_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


