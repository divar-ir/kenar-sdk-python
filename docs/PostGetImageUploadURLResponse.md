# PostGetImageUploadURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.post_get_image_upload_url_response import PostGetImageUploadURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetImageUploadURLResponse from a JSON string
post_get_image_upload_url_response_instance = PostGetImageUploadURLResponse.from_json(json)
# print the JSON string representation of the object
print(PostGetImageUploadURLResponse.to_json())

# convert the object into a dict
post_get_image_upload_url_response_dict = post_get_image_upload_url_response_instance.to_dict()
# create an instance of PostGetImageUploadURLResponse from a dict
post_get_image_upload_url_response_from_dict = PostGetImageUploadURLResponse.from_dict(post_get_image_upload_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


