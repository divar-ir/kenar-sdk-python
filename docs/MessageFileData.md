# MessageFileData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size_bytes** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.message_file_data import MessageFileData

# TODO update the JSON string below
json = "{}"
# create an instance of MessageFileData from a JSON string
message_file_data_instance = MessageFileData.from_json(json)
# print the JSON string representation of the object
print(MessageFileData.to_json())

# convert the object into a dict
message_file_data_dict = message_file_data_instance.to_dict()
# create an instance of MessageFileData from a dict
message_file_data_from_dict = MessageFileData.from_dict(message_file_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


