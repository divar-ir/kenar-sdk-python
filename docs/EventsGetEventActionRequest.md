# EventsGetEventActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | [**EventsGetEventActionRequestRequestData**](EventsGetEventActionRequestRequestData.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.events_get_event_action_request import EventsGetEventActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventsGetEventActionRequest from a JSON string
events_get_event_action_request_instance = EventsGetEventActionRequest.from_json(json)
# print the JSON string representation of the object
print(EventsGetEventActionRequest.to_json())

# convert the object into a dict
events_get_event_action_request_dict = events_get_event_action_request_instance.to_dict()
# create an instance of EventsGetEventActionRequest from a dict
events_get_event_action_request_from_dict = EventsGetEventActionRequest.from_dict(events_get_event_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


