# PostPostGeneralData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_slug** | **str** | نام دسته‌بندی هدف. دسته‌بندی‌های موجود را در این آدرس بیابید: https://kenar.divar.dev/openapi-doc/assets-get-categories/ | 
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
**video** | [**PostGeneralDataPostVideo**](PostGeneralDataPostVideo.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.post_post_general_data import PostPostGeneralData

# TODO update the JSON string below
json = "{}"
# create an instance of PostPostGeneralData from a JSON string
post_post_general_data_instance = PostPostGeneralData.from_json(json)
# print the JSON string representation of the object
print(PostPostGeneralData.to_json())

# convert the object into a dict
post_post_general_data_dict = post_post_general_data_instance.to_dict()
# create an instance of PostPostGeneralData from a dict
post_post_general_data_from_dict = PostPostGeneralData.from_dict(post_post_general_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


