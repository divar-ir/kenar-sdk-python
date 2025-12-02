# PostEditPostV2Body


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_data** | **object** | فیلدهای مختص دسته‌بندی که باید مطابق schema تکمیل شوند. schema را اینجا ببینید: https://kenar.divar.dev/openapi-doc/assets-get-submit-schema/ | [optional] 
**general_data** | [**PostPostGeneralData**](PostPostGeneralData.md) |  | [optional] 
**update_mask** | **List[str]** | مشخص می‌کند کدام فیلدها به‌روزرسانی شوند. از مسیرهای تودرتو مانند &#39;general_data.title&#39; یا &#39;category_data.price&#39; استفاده کنید. این کار تمایز بین پاک کردن یک فیلد و تغییر ندادن آن را ممکن می‌سازد. | 

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


