# MessageSender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | [**ChatapiMessageSenderSide**](ChatapiMessageSenderSide.md) |  | [optional] 
**type** | [**ChatapiMessageSenderType**](ChatapiMessageSenderType.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.message_sender import MessageSender

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSender from a JSON string
message_sender_instance = MessageSender.from_json(json)
# print the JSON string representation of the object
print(MessageSender.to_json())

# convert the object into a dict
message_sender_dict = message_sender_instance.to_dict()
# create an instance of MessageSender from a dict
message_sender_from_dict = MessageSender.from_dict(message_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


