# kenar_api_client.EventsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_register_event_subscription**](EventsApi.md#events_register_event_subscription) | **POST** /v1/open-platform/events/subscriptions | Subscribe to an event


# **events_register_event_subscription**
> object events_register_event_subscription(events_register_event_subscription_request)

Subscribe to an event

This requests allows you to subscribe to an event.
You need to send access-token in this API to check your access.
For subscribing on `NEW_MESSAGE_ON_POST` you need one of these scopes:
- CHAT_POST_CONVERSATIONS_READ.{post_token}
- CHAT_SUPPLIER_ALL_CONVERSATIONS_READ
For subscribing on `POST_UPDATE` you need `USER_POSTS_GET` scope.
After calling this API, You'll be notified in your webhook when corresponding event occurs.
Make sure webhook URL is set on providers panel for your app.
Some events are enabled by default and no subscription is needed for them(e.g chatbot messages).

### Example


```python
import kenar_api_client
from kenar_api_client.models.events_register_event_subscription_request import EventsRegisterEventSubscriptionRequest
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.EventsApi(api_client)
    events_register_event_subscription_request = kenar_api_client.EventsRegisterEventSubscriptionRequest() # EventsRegisterEventSubscriptionRequest | 

    try:
        # Subscribe to an event
        api_response = api_instance.events_register_event_subscription(events_register_event_subscription_request)
        print("The response of EventsApi->events_register_event_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_register_event_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events_register_event_subscription_request** | [**EventsRegisterEventSubscriptionRequest**](EventsRegisterEventSubscriptionRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

