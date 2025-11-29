# PostEditPostV2Body


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_data** | **object** | فیلدهای ویژه هر دسته‌بندی که باید مطابق قالب مشخص شده تکمیل شوند. قالب را از اینجا ببینید: https://kenar.divar.dev/openapi-doc/assets-get-submit-schema/ | [optional] 
**general_data** | [**PostPostGeneralData**](PostPostGeneralData.md) |  | [optional] 
**update_mask** | **List[str]** | فیلد ماسک مشخص می‌کند کدام فیلدها به‌روزرسانی شوند. از مسیرهای تو در تو برای هر دو general_data و category_data استفاده کنید (مثلاً، &#39;general_data.title&#39;، &#39;category_data.price&#39;). این امکان تمایز بین حذف یک فیلد و به‌روزرسانی نکردن آن را فراهم می‌کند. | 

## Example

```python
from kenar_api_client.models.post_edit_post_v2_body import PostEditPostV2Body

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditPostV2Body from a JSON string
post_edit_post_v2_body_instance = PostEditPostV2Body.from_json(json)
# print the JSON string representation of the object
print(PostEditPostV2Body.to_json())

# convert the object into a dict
post_edit_post_v2_body_dict = post_edit_post_v2_body_instance.to_dict()
# create an instance of PostEditPostV2Body from a dict
post_edit_post_v2_body_from_dict = PostEditPostV2Body.from_dict(post_edit_post_v2_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


