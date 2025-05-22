# PostEditPostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**image_paths** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.post_edit_post_body import PostEditPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of PostEditPostBody from a JSON string
post_edit_post_body_instance = PostEditPostBody.from_json(json)
# print the JSON string representation of the object
print(PostEditPostBody.to_json())

# convert the object into a dict
post_edit_post_body_dict = post_edit_post_body_instance.to_dict()
# create an instance of PostEditPostBody from a dict
post_edit_post_body_from_dict = PostEditPostBody.from_dict(post_edit_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


