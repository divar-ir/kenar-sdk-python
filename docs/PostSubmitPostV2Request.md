# PostSubmitPostV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_fields** | **object** | فیلدهای ویژه هر دسته‌بندی که باید مطابق قالب مشخص شده تکمیل شوند. قالب را از اینجا ببینید: https://divar-ir.github.io/kenar-docs/openapi-doc/assets-get-submit-schema/ | 
**general_data** | [**PostSubmitPostGeneralData**](PostSubmitPostGeneralData.md) |  | 
**landline_numbers** | **List[str]** | Landline numbers to be added to the post | [optional] 

## Example

```python
from kenar_api_client.models.post_submit_post_v2_request import PostSubmitPostV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of PostSubmitPostV2Request from a JSON string
post_submit_post_v2_request_instance = PostSubmitPostV2Request.from_json(json)
# print the JSON string representation of the object
print(PostSubmitPostV2Request.to_json())

# convert the object into a dict
post_submit_post_v2_request_dict = post_submit_post_v2_request_instance.to_dict()
# create an instance of PostSubmitPostV2Request from a dict
post_submit_post_v2_request_from_dict = PostSubmitPostV2Request.from_dict(post_submit_post_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


