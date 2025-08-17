# WidgetsAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_pop_link** | **bool** | deprecated; use is_new_flow &#x3D; 1 in PagePresentation instead. | [optional] 
**payload** | [**ProtobufAny**](ProtobufAny.md) |  | [optional] 
**type** | [**WidgetsActionType**](WidgetsActionType.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.widgets_action import WidgetsAction

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetsAction from a JSON string
widgets_action_instance = WidgetsAction.from_json(json)
# print the JSON string representation of the object
print(WidgetsAction.to_json())

# convert the object into a dict
widgets_action_dict = widgets_action_instance.to_dict()
# create an instance of WidgetsAction from a dict
widgets_action_from_dict = WidgetsAction.from_dict(widgets_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


