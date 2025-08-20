# PostTemporaryResidenceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **int** | متراژ اقامتگاه به متر مربع | [optional] 
**check_in_time** | **str** | Check-in time | [optional] 
**check_out_time** | **str** | Check-out time | [optional] 
**comfort_amenities** | [**List[TemporaryResidenceFieldsComfortAmenity]**](TemporaryResidenceFieldsComfortAmenity.md) |  | [optional] 
**damage_deposit** | **str** | Damage deposit amount in Toman | [optional] 
**extra_person_capacity** | **int** | تعداد افراد اضافه مجاز در اقامتگاه | [optional] 
**fully_furnished** | **bool** | Whether the residence is fully furnished | [optional] 
**has_own_image** | **bool** | تصاویر مربوط به خود ملک بوده و تزئینی نیستند. | [optional] 
**heating_cooling_system** | [**List[TemporaryResidenceFieldsHeatingCoolingSystem]**](TemporaryResidenceFieldsHeatingCoolingSystem.md) |  | [optional] 
**house_rules** | **str** | House rules and regulations | [optional] 
**minimum_stay** | **int** | Minimum number of days required for stay | [optional] 
**pets_allowed** | [**TemporaryResidenceFieldsPetsAllowed**](TemporaryResidenceFieldsPetsAllowed.md) |  | [optional] 
**price_cost_per_extra_person** | **str** | هزینه هر نفر اضافه به ازای هر شب به تومان | [optional] 
**price_regular_days** | **str** | قیمت اقامتگاه در روزهای عادی (شنبه تا سه‌شنبه) به تومان | [optional] 
**price_special_days** | **str** | قیمت اقامتگاه در روزهای خاص (تعطیلات و مناسبت‌ها) به تومان | [optional] 
**price_weekends** | **str** | قیمت اقامتگاه در آخر هفته (چهارشنبه تا جمعه) به تومان | [optional] 
**regular_person_capacity** | **int** | ظرفیت استاندارد افراد در اقامتگاه | [optional] 
**rental_period** | [**TemporaryResidenceFieldsRentalPeriod**](TemporaryResidenceFieldsRentalPeriod.md) |  | [optional] 
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


