# MessageVoiceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**size_bytes** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.message_voice_data import MessageVoiceData

# TODO update the JSON string below
json = "{}"
# create an instance of MessageVoiceData from a JSON string
message_voice_data_instance = MessageVoiceData.from_json(json)
# print the JSON string representation of the object
print(MessageVoiceData.to_json())

# convert the object into a dict
message_voice_data_dict = message_voice_data_instance.to_dict()
# create an instance of MessageVoiceData from a dict
message_voice_data_from_dict = MessageVoiceData.from_dict(message_voice_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


