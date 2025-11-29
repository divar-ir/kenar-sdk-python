# GetUploadURLsV2ResponseUploadFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_method** | [**OpenPlatformpostHTTPMethod**](OpenPlatformpostHTTPMethod.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.get_upload_urls_v2_response_upload_format import GetUploadURLsV2ResponseUploadFormat

# TODO update the JSON string below
json = "{}"
# create an instance of GetUploadURLsV2ResponseUploadFormat from a JSON string
get_upload_urls_v2_response_upload_format_instance = GetUploadURLsV2ResponseUploadFormat.from_json(json)
# print the JSON string representation of the object
print(GetUploadURLsV2ResponseUploadFormat.to_json())

# convert the object into a dict
get_upload_urls_v2_response_upload_format_dict = get_upload_urls_v2_response_upload_format_instance.to_dict()
# create an instance of GetUploadURLsV2ResponseUploadFormat from a dict
get_upload_urls_v2_response_upload_format_from_dict = GetUploadURLsV2ResponseUploadFormat.from_dict(get_upload_urls_v2_response_upload_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


