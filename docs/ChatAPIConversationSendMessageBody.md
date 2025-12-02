# ChatAPIConversationSendMessageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_token** | **str** | توکن فایل ضمیمه شده (در صورت وجود) | [optional] 
**message** | **str** | محتوای پیام متنی برای ارسال | 
**receiver_buttons** | [**ChatapiChatButtonGrid**](ChatapiChatButtonGrid.md) |  | [optional] 
**sender_buttons** | [**ChatapiChatButtonGrid**](ChatapiChatButtonGrid.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.chat_api_conversation_send_message_body import ChatAPIConversationSendMessageBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChatAPIConversationSendMessageBody from a JSON string
chat_api_conversation_send_message_body_instance = ChatAPIConversationSendMessageBody.from_json(json)
# print the JSON string representation of the object
print(ChatAPIConversationSendMessageBody.to_json())

# convert the object into a dict
chat_api_conversation_send_message_body_dict = chat_api_conversation_send_message_body_instance.to_dict()
# create an instance of ChatAPIConversationSendMessageBody from a dict
chat_api_conversation_send_message_body_from_dict = ChatAPIConversationSendMessageBody.from_dict(chat_api_conversation_send_message_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


