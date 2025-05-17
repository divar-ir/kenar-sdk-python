# ChatapiConversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**ChatapiConversationType**](ChatapiConversationType.md) |  | [optional] 
**post_token** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.chatapi_conversation import ChatapiConversation

# TODO update the JSON string below
json = "{}"
# create an instance of ChatapiConversation from a JSON string
chatapi_conversation_instance = ChatapiConversation.from_json(json)
# print the JSON string representation of the object
print(ChatapiConversation.to_json())

# convert the object into a dict
chatapi_conversation_dict = chatapi_conversation_instance.to_dict()
# create an instance of ChatapiConversation from a dict
chatapi_conversation_from_dict = ChatapiConversation.from_dict(chatapi_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


