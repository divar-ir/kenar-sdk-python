# WidgetsGeneralNetworkCallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_action** | [**WidgetsAction**](WidgetsAction.md) |  | [optional] 
**toast_message** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.widgets_general_network_call_response import WidgetsGeneralNetworkCallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetsGeneralNetworkCallResponse from a JSON string
widgets_general_network_call_response_instance = WidgetsGeneralNetworkCallResponse.from_json(json)
# print the JSON string representation of the object
print(WidgetsGeneralNetworkCallResponse.to_json())

# convert the object into a dict
widgets_general_network_call_response_dict = widgets_general_network_call_response_instance.to_dict()
# create an instance of WidgetsGeneralNetworkCallResponse from a dict
widgets_general_network_call_response_from_dict = WidgetsGeneralNetworkCallResponse.from_dict(widgets_general_network_call_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


