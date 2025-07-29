# PostTemporaryResidenceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **int** | Area of the residence in square meters | [optional] 
**extra_person_capacity** | **int** | Number of allowed extra people that can stay in the residence | [optional] 
**has_own_image** | **bool** | Whether the images are of the property itself and not decorative/stock photos. | [optional] 
**price_cost_per_extra_person** | **str** | Cost per extra person per night in Toman | [optional] 
**price_regular_days** | **str** | Price of the residence for regular days (Saturday to Tuesday) in Toman | [optional] 
**price_special_days** | **str** | Price of the residence for special days (holidays and occasions) in Toman | [optional] 
**price_weekends** | **str** | Price of the residence for weekends (Wednesday to Friday) in Toman | [optional] 
**regular_person_capacity** | **int** | Number of allowed regular people that can stay in the residence | [optional] 
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


