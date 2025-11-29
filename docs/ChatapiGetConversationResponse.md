# ChatapiGetConversationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ChatapiConversation**](ChatapiConversation.md) |  | 
**messages** | [**List[ChatapiMessage]**](ChatapiMessage.md) | فهرست پیام‌های مکالمه | 

## Example

```python
from kenar_api_client.models.chatapi_get_conversation_response import ChatapiGetConversationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatapiGetConversationResponse from a JSON string
chatapi_get_conversation_response_instance = ChatapiGetConversationResponse.from_json(json)
# print the JSON string representation of the object
print(ChatapiGetConversationResponse.to_json())

# convert the object into a dict
chatapi_get_conversation_response_dict = chatapi_get_conversation_response_instance.to_dict()
# create an instance of ChatapiGetConversationResponse from a dict
chatapi_get_conversation_response_from_dict = ChatapiGetConversationResponse.from_dict(chatapi_get_conversation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


