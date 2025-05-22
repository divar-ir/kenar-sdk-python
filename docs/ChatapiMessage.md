# ChatapiMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ChatapiConversation**](ChatapiConversation.md) |  | [optional] 
**file_data** | [**MessageFileData**](MessageFileData.md) |  | [optional] 
**id** | **str** |  | [optional] 
**image_data** | [**MessageImageData**](MessageImageData.md) |  | [optional] 
**location_data** | [**MessageLocationData**](MessageLocationData.md) |  | [optional] 
**sender** | [**MessageSender**](MessageSender.md) |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**text** | **str** |  | [optional] 
**type** | [**ChatapiMessageType**](ChatapiMessageType.md) |  | [optional] 
**video_data** | [**MessageVideoData**](MessageVideoData.md) |  | [optional] 
**voice_data** | [**MessageVoiceData**](MessageVoiceData.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.chatapi_message import ChatapiMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatapiMessage from a JSON string
chatapi_message_instance = ChatapiMessage.from_json(json)
# print the JSON string representation of the object
print(ChatapiMessage.to_json())

# convert the object into a dict
chatapi_message_dict = chatapi_message_instance.to_dict()
# create an instance of ChatapiMessage from a dict
chatapi_message_from_dict = ChatapiMessage.from_dict(chatapi_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


