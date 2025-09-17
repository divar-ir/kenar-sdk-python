# PostSubmitUserPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_fields** | **object** | فیلدهای ویژه هر دسته‌بندی که باید مطابق قالب مشخص شده تکمیل شوند. قالب را از اینجا ببینید: https://divar-ir.github.io/kenar-docs/openapi-doc/assets-get-submit-schema/ | 
**general_data** | [**PostSubmitPostGeneralData**](PostSubmitPostGeneralData.md) |  | 

## Example

```python
from kenar_api_client.models.post_submit_user_post_request import PostSubmitUserPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSubmitUserPostRequest from a JSON string
post_submit_user_post_request_instance = PostSubmitUserPostRequest.from_json(json)
# print the JSON string representation of the object
print(PostSubmitUserPostRequest.to_json())

# convert the object into a dict
post_submit_user_post_request_dict = post_submit_user_post_request_instance.to_dict()
# create an instance of PostSubmitUserPostRequest from a dict
post_submit_user_post_request_from_dict = PostSubmitUserPostRequest.from_dict(post_submit_user_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


