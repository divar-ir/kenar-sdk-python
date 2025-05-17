# ChatapiChatButtonRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buttons** | [**List[ChatapiChatButton]**](ChatapiChatButton.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.chatapi_chat_button_row import ChatapiChatButtonRow

# TODO update the JSON string below
json = "{}"
# create an instance of ChatapiChatButtonRow from a JSON string
chatapi_chat_button_row_instance = ChatapiChatButtonRow.from_json(json)
# print the JSON string representation of the object
print(ChatapiChatButtonRow.to_json())

# convert the object into a dict
chatapi_chat_button_row_dict = chatapi_chat_button_row_instance.to_dict()
# create an instance of ChatapiChatButtonRow from a dict
chatapi_chat_button_row_from_dict = ChatapiChatButtonRow.from_dict(chatapi_chat_button_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


