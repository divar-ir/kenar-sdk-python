# EventsEventButtonList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EventsEventButton]**](EventsEventButton.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.events_event_button_list import EventsEventButtonList

# TODO update the JSON string below
json = "{}"
# create an instance of EventsEventButtonList from a JSON string
events_event_button_list_instance = EventsEventButtonList.from_json(json)
# print the JSON string representation of the object
print(EventsEventButtonList.to_json())

# convert the object into a dict
events_event_button_list_dict = events_event_button_list_instance.to_dict()
# create an instance of EventsEventButtonList from a dict
events_event_button_list_from_dict = EventsEventButtonList.from_dict(events_event_button_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


