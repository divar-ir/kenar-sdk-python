# SemanticCreatePostSemanticBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **int** | هزینه مرتبط با عملیات | [optional] 
**semantic** | **Dict[str, str]** | مپ key-value اطلاعات معنایی برای ذخیره | 
**ticket_uuid** | **str** | UUID تیکت پرداخت (اختیاری) | [optional] 

## Example

```python
from kenar_api_client.models.semantic_create_post_semantic_body import SemanticCreatePostSemanticBody

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticCreatePostSemanticBody from a JSON string
semantic_create_post_semantic_body_instance = SemanticCreatePostSemanticBody.from_json(json)
# print the JSON string representation of the object
print(SemanticCreatePostSemanticBody.to_json())

# convert the object into a dict
semantic_create_post_semantic_body_dict = semantic_create_post_semantic_body_instance.to_dict()
# create an instance of SemanticCreatePostSemanticBody from a dict
semantic_create_post_semantic_body_from_dict = SemanticCreatePostSemanticBody.from_dict(semantic_create_post_semantic_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


