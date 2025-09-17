# PostSubmitPostGeneralData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_slug** | **str** | نام دسته‌بندی هدف. دسته‌بندی‌های موجود را در این آدرس بیابید: https://divar-ir.github.io/kenar-docs/openapi-doc/assets-get-categories/ | 
**chat_enabled** | **bool** | امکان چت فعال باشد | 
**city** | **str** | شهر آگهی | 
**description** | **str** | توضیحات آگهی | 
**district** | **str** | محله آگهی | [optional] 
**hide_phone** | **bool** | عدم نمایش شماره تماس به کاربران | 
**images** | **List[str]** |  | 
**latitude** | **float** | عرض جغرافیایی آگهی | [optional] 
**location_type** | [**PostLocationType**](PostLocationType.md) |  | 
**longitude** | **float** | طول جغرافیایی آگهی | [optional] 
**title** | **str** | عنوان آگهی | 

## Example

```python
from kenar_api_client.models.post_submit_post_general_data import PostSubmitPostGeneralData

# TODO update the JSON string below
json = "{}"
# create an instance of PostSubmitPostGeneralData from a JSON string
post_submit_post_general_data_instance = PostSubmitPostGeneralData.from_json(json)
# print the JSON string representation of the object
print(PostSubmitPostGeneralData.to_json())

# convert the object into a dict
post_submit_post_general_data_dict = post_submit_post_general_data_instance.to_dict()
# create an instance of PostSubmitPostGeneralData from a dict
post_submit_post_general_data_from_dict = PostSubmitPostGeneralData.from_dict(post_submit_post_general_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


