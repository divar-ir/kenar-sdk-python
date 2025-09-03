# PostHomePresellFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_price_per_square_meter** | **str** | Base price per square meter in Toman | [optional] 
**construction_phase** | [**HomePresellFieldsConstructionPhase**](HomePresellFieldsConstructionPhase.md) |  | [optional] 
**delivery_month** | [**HomePresellFieldsDeliveryMonth**](HomePresellFieldsDeliveryMonth.md) |  | [optional] 
**delivery_payment_percentage** | **int** | Payment percentage required upon delivery | [optional] 
**delivery_year** | [**HomePresellFieldsDeliveryYear**](HomePresellFieldsDeliveryYear.md) |  | [optional] 
**developer_company_name** | **str** | Name of the developer company | [optional] 
**down_payment_percentage** | **int** | Down payment percentage required | [optional] 
**has_own_image** | **bool** | تصاویر مربوط به خود ملک بوده و تزئینی نیستند. | 
**min_unit_size** | **int** | Minimum unit size in square meters | [optional] 
**project_name** | **str** | Name of the home presell project | [optional] 
**project_physical_progress_percentage** | **int** | Physical progress percentage of the project | [optional] 
**unit_types_offered** | [**List[HomePresellFieldsUnitType]**](HomePresellFieldsUnitType.md) | List of unit types offered in the project | [optional] 

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


