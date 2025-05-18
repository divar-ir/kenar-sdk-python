# AddonsAction

Represents an action that can be performed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_direct_link** | **str** | An action to send user to your URL directly with just a resource id (if applicable) | [optional] 
**open_server_link** | [**AddonsOpenServerLink**](AddonsOpenServerLink.md) |  | [optional] 
**get_dynamic_action** | [**AddonsGetDynamicAction**](AddonsGetDynamicAction.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_action import AddonsAction

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsAction from a JSON string
addons_action_instance = AddonsAction.from_json(json)
# print the JSON string representation of the object
print(AddonsAction.to_json())

# convert the object into a dict
addons_action_dict = addons_action_instance.to_dict()
# create an instance of AddonsAction from a dict
addons_action_from_dict = AddonsAction.from_dict(addons_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


