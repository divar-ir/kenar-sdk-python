# ChatAPIChatBotSendMessageBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buttons** | [**ChatapiChatButtonGrid**](ChatapiChatButtonGrid.md) |  | [optional] 
**media_token** | **str** | توکن فایل ضمیمه شده (در صورت وجود) | [optional] 
**text_message** | **str** | محتوای پیام متنی برای ارسال توسط ربات | 
**user_id** | **str** | شناسه منحصر به فرد کاربر برای شروع یا ادامه مکالمه | [optional] 

## Example

```python
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChatAPIChatBotSendMessageBody from a JSON string
chat_api_chat_bot_send_message_body_instance = ChatAPIChatBotSendMessageBody.from_json(json)
# print the JSON string representation of the object
print(ChatAPIChatBotSendMessageBody.to_json())

# convert the object into a dict
chat_api_chat_bot_send_message_body_dict = chat_api_chat_bot_send_message_body_instance.to_dict()
# create an instance of ChatAPIChatBotSendMessageBody from a dict
chat_api_chat_bot_send_message_body_from_dict = ChatAPIChatBotSendMessageBody.from_dict(chat_api_chat_bot_send_message_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


