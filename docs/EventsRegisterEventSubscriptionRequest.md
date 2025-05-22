# EventsRegisterEventSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_resource_id** | **str** |  | [optional] 
**event_type** | [**EventsRegisterEventSubscriptionRequestEventType**](EventsRegisterEventSubscriptionRequestEventType.md) |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from kenar_api_client.models.events_register_event_subscription_request import EventsRegisterEventSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventsRegisterEventSubscriptionRequest from a JSON string
events_register_event_subscription_request_instance = EventsRegisterEventSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(EventsRegisterEventSubscriptionRequest.to_json())

# convert the object into a dict
events_register_event_subscription_request_dict = events_register_event_subscription_request_instance.to_dict()
# create an instance of EventsRegisterEventSubscriptionRequest from a dict
events_register_event_subscription_request_from_dict = EventsRegisterEventSubscriptionRequest.from_dict(events_register_event_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


