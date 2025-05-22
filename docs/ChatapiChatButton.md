# ChatapiChatButton


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AddonsAction**](AddonsAction.md) |  | [optional] 
**caption** | **str** |  | [optional] 
**icon** | [**DivarIconsIconName**](DivarIconsIconName.md) |  | [optional] 
**icon_name** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.chatapi_chat_button import ChatapiChatButton

# TODO update the JSON string below
json = "{}"
# create an instance of ChatapiChatButton from a JSON string
chatapi_chat_button_instance = ChatapiChatButton.from_json(json)
# print the JSON string representation of the object
print(ChatapiChatButton.to_json())

# convert the object into a dict
chatapi_chat_button_dict = chatapi_chat_button_instance.to_dict()
# create an instance of ChatapiChatButton from a dict
chatapi_chat_button_from_dict = ChatapiChatButton.from_dict(chatapi_chat_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


