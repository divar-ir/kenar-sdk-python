# MessageContactData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.message_contact_data import MessageContactData

# TODO update the JSON string below
json = "{}"
# create an instance of MessageContactData from a JSON string
message_contact_data_instance = MessageContactData.from_json(json)
# print the JSON string representation of the object
print(MessageContactData.to_json())

# convert the object into a dict
message_contact_data_dict = message_contact_data_instance.to_dict()
# create an instance of MessageContactData from a dict
message_contact_data_from_dict = MessageContactData.from_dict(message_contact_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


