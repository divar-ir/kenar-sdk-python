# MessageVideoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**size_bytes** | **str** |  | [optional] 
**thumbnail_link** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.message_video_data import MessageVideoData

# TODO update the JSON string below
json = "{}"
# create an instance of MessageVideoData from a JSON string
message_video_data_instance = MessageVideoData.from_json(json)
# print the JSON string representation of the object
print(MessageVideoData.to_json())

# convert the object into a dict
message_video_data_dict = message_video_data_instance.to_dict()
# create an instance of MessageVideoData from a dict
message_video_data_from_dict = MessageVideoData.from_dict(message_video_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


