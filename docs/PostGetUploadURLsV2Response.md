# PostGetUploadURLsV2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**GetUploadURLsV2ResponseUploadFormat**](GetUploadURLsV2ResponseUploadFormat.md) |  | [optional] 
**video** | [**GetUploadURLsV2ResponseUploadFormat**](GetUploadURLsV2ResponseUploadFormat.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.post_get_upload_urls_v2_response import PostGetUploadURLsV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetUploadURLsV2Response from a JSON string
post_get_upload_urls_v2_response_instance = PostGetUploadURLsV2Response.from_json(json)
# print the JSON string representation of the object
print(PostGetUploadURLsV2Response.to_json())

# convert the object into a dict
post_get_upload_urls_v2_response_dict = post_get_upload_urls_v2_response_instance.to_dict()
# create an instance of PostGetUploadURLsV2Response from a dict
post_get_upload_urls_v2_response_from_dict = PostGetUploadURLsV2Response.from_dict(post_get_upload_urls_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


