# EventsEventButton


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AddonsAction**](AddonsAction.md) |  | [optional] 
**title** | **str** | The text to display on the button | [optional] 

## Example

```python
from kenar_api_client.models.events_event_button import EventsEventButton

# TODO update the JSON string below
json = "{}"
# create an instance of EventsEventButton from a JSON string
events_event_button_instance = EventsEventButton.from_json(json)
# print the JSON string representation of the object
print(EventsEventButton.to_json())

# convert the object into a dict
events_event_button_dict = events_event_button_instance.to_dict()
# create an instance of EventsEventButton from a dict
events_event_button_from_dict = EventsEventButton.from_dict(events_event_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


