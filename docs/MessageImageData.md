# MessageImageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height_px** | **int** |  | [optional] 
**link** | **str** |  | [optional] 
**size_bytes** | **str** |  | [optional] 
**width_px** | **int** |  | [optional] 

## Example

```python
from kenar_api_client.models.message_image_data import MessageImageData

# TODO update the JSON string below
json = "{}"
# create an instance of MessageImageData from a JSON string
message_image_data_instance = MessageImageData.from_json(json)
# print the JSON string representation of the object
print(MessageImageData.to_json())

# convert the object into a dict
message_image_data_dict = message_image_data_instance.to_dict()
# create an instance of MessageImageData from a dict
message_image_data_from_dict = MessageImageData.from_dict(message_image_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


