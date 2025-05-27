# MessageLocationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | عرض جغرافیایی به درجه. باید در محدوده [-90.0, +90.0] باشد. | [optional] 
**longitude** | **float** | طول جغرافیایی به درجه. باید در محدوده [-180.0, +180.0] باشد. | [optional] 

## Example

```python
from kenar_api_client.models.message_location_data import MessageLocationData

# TODO update the JSON string below
json = "{}"
# create an instance of MessageLocationData from a JSON string
message_location_data_instance = MessageLocationData.from_json(json)
# print the JSON string representation of the object
print(MessageLocationData.to_json())

# convert the object into a dict
message_location_data_dict = message_location_data_instance.to_dict()
# create an instance of MessageLocationData from a dict
message_location_data_from_dict = MessageLocationData.from_dict(message_location_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


