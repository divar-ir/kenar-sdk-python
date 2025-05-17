# ChatapiConversationSendMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.chatapi_conversation_send_message_response import ChatapiConversationSendMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatapiConversationSendMessageResponse from a JSON string
chatapi_conversation_send_message_response_instance = ChatapiConversationSendMessageResponse.from_json(json)
# print the JSON string representation of the object
print(ChatapiConversationSendMessageResponse.to_json())

# convert the object into a dict
chatapi_conversation_send_message_response_dict = chatapi_conversation_send_message_response_instance.to_dict()
# create an instance of ChatapiConversationSendMessageResponse from a dict
chatapi_conversation_send_message_response_from_dict = ChatapiConversationSendMessageResponse.from_dict(chatapi_conversation_send_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


