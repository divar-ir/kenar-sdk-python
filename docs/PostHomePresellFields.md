# PostHomePresellFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_price_per_square_meter** | **str** | قیمت پایه هر متر مربع به تومان | [optional] 
**construction_phase** | [**HomePresellFieldsConstructionPhase**](HomePresellFieldsConstructionPhase.md) |  | [optional] 
**delivery_month** | [**HomePresellFieldsDeliveryMonth**](HomePresellFieldsDeliveryMonth.md) |  | [optional] 
**delivery_payment_percentage** | **int** | درصد پرداخت مورد نیاز در زمان تحویل | [optional] 
**delivery_year** | [**HomePresellFieldsDeliveryYear**](HomePresellFieldsDeliveryYear.md) |  | [optional] 
**developer_company_name** | **str** | نام شرکت سازنده | [optional] 
**down_payment_percentage** | **int** | درصد پیش پرداخت اولیه | [optional] 
**has_own_image** | **bool** | آیا تصاویر واقعی ملک هستند (نه تزئینی) | 
**min_unit_size** | **int** | حداقل مساحت واحد بر حسب متر مربع | [optional] 
**project_name** | **str** | نام پروژه پیش‌فروش مسکن | [optional] 
**project_physical_progress_percentage** | **int** | درصد پیشرفت فیزیکی پروژه | [optional] 
**unit_types_offered** | [**List[HomePresellFieldsUnitType]**](HomePresellFieldsUnitType.md) | فهرست انواع واحد ارائه شده در پروژه | [optional] 

## Example

```python
from kenar_api_client.models.post_home_presell_fields import PostHomePresellFields

# TODO update the JSON string below
json = "{}"
# create an instance of PostHomePresellFields from a JSON string
post_home_presell_fields_instance = PostHomePresellFields.from_json(json)
# print the JSON string representation of the object
print(PostHomePresellFields.to_json())

# convert the object into a dict
post_home_presell_fields_dict = post_home_presell_fields_instance.to_dict()
# create an instance of PostHomePresellFields from a dict
post_home_presell_fields_from_dict = PostHomePresellFields.from_dict(post_home_presell_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


