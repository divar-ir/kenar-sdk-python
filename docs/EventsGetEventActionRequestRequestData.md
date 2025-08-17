# EventsGetEventActionRequestRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.events_get_event_action_request_request_data import EventsGetEventActionRequestRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of EventsGetEventActionRequestRequestData from a JSON string
events_get_event_action_request_request_data_instance = EventsGetEventActionRequestRequestData.from_json(json)
# print the JSON string representation of the object
print(EventsGetEventActionRequestRequestData.to_json())

# convert the object into a dict
events_get_event_action_request_request_data_dict = events_get_event_action_request_request_data_instance.to_dict()
# create an instance of EventsGetEventActionRequestRequestData from a dict
events_get_event_action_request_request_data_from_dict = EventsGetEventActionRequestRequestData.from_dict(events_get_event_action_request_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


