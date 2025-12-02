# ChatapiGenerateUploadTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | توکن با کدگذاری base64 که می‌توان در endpoint آپلود از آن استفاده کرد | [optional] [readonly] 

## Example

```python
from kenar_api_client.models.chatapi_generate_upload_token_response import ChatapiGenerateUploadTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatapiGenerateUploadTokenResponse from a JSON string
chatapi_generate_upload_token_response_instance = ChatapiGenerateUploadTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ChatapiGenerateUploadTokenResponse.to_json())

# convert the object into a dict
chatapi_generate_upload_token_response_dict = chatapi_generate_upload_token_response_instance.to_dict()
# create an instance of ChatapiGenerateUploadTokenResponse from a dict
chatapi_generate_upload_token_response_from_dict = ChatapiGenerateUploadTokenResponse.from_dict(chatapi_generate_upload_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


